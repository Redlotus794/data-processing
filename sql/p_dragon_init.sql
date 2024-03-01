use p_dragon;

-- 创建dkb
create table dragon_knowledge_base
(
	id serial not null
		constraint dragon_knowledge_base_pk
			primary key,
	hash varchar(255) not null,
	name varchar(255) not null,
	content text,
	create_time timestamp default CURRENT_TIMESTAMP,
    update_time timestamp default CURRENT_TIMESTAMP
);

alter table dragon_knowledge_base owner to wangjialong;

create unique index dragon_knowledge_base_hash_uindex
	on dragon_knowledge_base (hash);

create unique index dragon_knowledge_base_name_uindex
	on dragon_knowledge_base (name);


-- 创建dvl
create table p_dragon.dragon_version_log
(
	id serial not null
		constraint dragon_version_log_pk
			primary key,
	hash varchar(255) not null,
	name varchar(255) not null,
	content text,
	create_time timestamp default CURRENT_TIMESTAMP,
	update_time timestamp default CURRENT_TIMESTAMP
);

alter table p_dragon.dragon_version_log owner to wangjialong;

create unique index dragon_version_log_hash_uindex
	on p_dragon.dragon_version_log (hash);

create unique index dragon_version_log_name_uindex
	on p_dragon.dragon_version_log (name);


-- dvl_v2
create table p_dragon.dragon_version_log_v2
(
	id serial not null
		constraint dragon_version_log_v2_pk
			primary key,
	hash varchar(255) not null,
	name varchar(255) not null,
	content text,
	create_time timestamp default CURRENT_TIMESTAMP,
	update_time timestamp default CURRENT_TIMESTAMP
);

alter table p_dragon.dragon_version_log_v2 owner to wangjialong;

create unique index dragon_version_log_v2_hash_uindex
	on p_dragon.dragon_version_log_v2 (hash);

create unique index dragon_version_log_v2_name_uindex
	on p_dragon.dragon_version_log_v2 (name);


