from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility, MilvusClient
from config.settings import Settings
import re

class MilvusConn:
    """
    Milvus的连接池对象
    """

    def __init__(self, collection_name = 'dkb', dim = 768):
        """
        初始化
        如果milvus不存在collection，则创建一个
        """
        connections.connect(host=Settings.MILVUS_URL, port=Settings.MILVUS_PORT)
        self.client = MilvusClient(host=Settings.MILVUS_URL, port=Settings.MILVUS_PORT)
        self.collection_name = collection_name
        self.dim = dim
        self.__create_milvus_collection_if_necessary()
        # 创建后，可以定义Collection
        self.collection = Collection(collection_name)


    def drop_collection(self):
        """
        删除一个集合
        """
        if utility.has_collection(self.collection_name):
            self.client.drop_collection(collection_name = self.collection_name)
            return 1
        else:
            return 0


    def flush(self):
        self.client.flush(collection_name = self.collection_name)
        
    
    def num_entities(self):
        """
        collection的实体数量

        :return -1 表示不存在
        """
        if not utility.has_collection(self.collection_name):
            return -1
            
        return self.client.num_entities(collection_name = self.collection_name)


    def get(self, ids):
        """
        基于id查询实体数据
        """
        self.client.get(collection_name = self.collection_name, ids = ids)
        
    
    def stats(self):
        """
        Connection的状态
        """
        print(f"current collection name {self.collection_name}")
        print(f"num of entities is {self.client.num_entities(self.collection_name)}")


    def insert(self, data):
        print(f"insert entities")
        self.collection.insert(data)
        self.client.flush(collection_name = self.collection_name)
    
    
    def __create_milvus_collection_if_necessary(self):
        """
        创建milvus的collection
        """
        if utility.has_collection(self.collection_name):        
            return
        
        if self.collection_name == 'dkb_v1':
            self.__dkb_v1_collection()
        elif re.match(r'^dvl_', self.collection_name):
            self.__dvl_collection()
        else:
            self.__default_collection()


    def __dvl_collection(self):
        print("创建Dragon Version Log向量数据库")
        fields = [
            FieldSchema(name='id', dtype=DataType.INT64, descrition='ids', is_primary=True, auto_id=True),
            FieldSchema(name='name', dtype=DataType.VARCHAR, max_length=255, descrition='document name'),
            FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, descrition='embedding vectors', dim=self.dim)
        ]
        schema = CollectionSchema(fields=fields, description='reverse image search')
        collection = Collection(name=self.collection_name, schema=schema)
        # create IVF_FLAT index for collection.
        index_params = {
            'metric_type':'L2',
            'index_type':"IVF_FLAT",
            'params':{"nlist":2048}
        }
        collection.create_index(field_name="embedding", index_params=index_params)   
        return collection

    def __dkb_v1_collection(self):
        print("创建dkb_v1向量数据库")
        fields = [
            FieldSchema(name='id', dtype=DataType.INT64, descrition='ids', is_primary=True, auto_id=True),
            FieldSchema(name='name', dtype=DataType.VARCHAR, max_length=255, descrition='document name'),
            FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, descrition='embedding vectors', dim=self.dim)
        ]
        schema = CollectionSchema(fields=fields, description='reverse image search')
        collection = Collection(name=self.collection_name, schema=schema)
        # create IVF_FLAT index for collection.
        index_params = {
            'metric_type':'L2',
            'index_type':"IVF_FLAT",
            'params':{"nlist":2048}
        }
        collection.create_index(field_name="embedding", index_params=index_params)   
        return collection
    

    def __default_collection(self):     
        print("创建默认向量数据库")
        fields = [
        FieldSchema(name='id', dtype=DataType.INT64, descrition='ids', is_primary=True, auto_id=False),
        FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, descrition='embedding vectors', dim=self.dim)
        ]
        schema = CollectionSchema(fields=fields, description='reverse image search')
        collection = Collection(name=self.collection_name, schema=schema)
    
        # create IVF_FLAT index for collection.
        index_params = {
            'metric_type':'L2',
            'index_type':"IVF_FLAT",
            'params':{"nlist":2048}
        }
        collection.create_index(field_name="embedding", index_params=index_params)   
        return collection
