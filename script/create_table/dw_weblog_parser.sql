

DROP TABLE IF EXISTS dw_weblog_parser;
CREATE TABLE dw_weblog_parser(
    ip STRING COMMENT 'client ip address',
    user STRING,
    time DATETIME,
    method STRING COMMENT 'HTTP request type, such as GET POST...',
    url STRING,
    protocol STRING,
    status BIGINT COMMENT 'HTTP reponse code from server',
    size BIGINT,
    referer STRING,
    agent STRING)
PARTITIONED BY(dt STRING);


ALTER TABLE dw_log_parser ADD IF NOT EXISTS PARTITION (dt='$bizdate$');

INSERT OVERWRITE TABLE dw_log_parser PARTITION(dt='$bizdate$')
SELECT 
    ip, 
    user, 
    time,
    regexp_substr(request, "(^[^ ]+ )") as method,
    regexp_extract(request, "^[^ ]+ (.*) [^ ]+$") as url,
    regexp_substr(request, "([^ ]+$)") as protocol,
    status, 
    size, 
    referer, 
    agent
FROM ods_weblog
WHERE dt='$bizdate$';

