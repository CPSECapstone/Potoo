create table Video_meta_data(
	file_format varchar(99),
    recording_length decimal(65, 2),
    timestamp DateTime
);


create table records(
	timestamp DateTime, 
    agent varchar(99),
    customer_name varchar(99),
    customer_phone varchar(99),
    source_url varchar(99),
    meta_data varchar(99),
    Primary key (timestamp, agent),
	Unique (source),
	Foreign key (meta_data) references Video_Meta_data (id)
);

