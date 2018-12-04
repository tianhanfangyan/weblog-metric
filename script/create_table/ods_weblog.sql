DROP TABLE IF EXISTS ods_weblog;
CREATE TABLE ods_weblog(
    ip STRING COMMENT 'IP地址',
    user STRING COMMENT '用户名',
    time DATETIME COMMENT '访问时间',
    request STRING COMMENT '请求页面：HTTP request type + requested path without args + HTTP protocol version',
    status BIGINT COMMENT '请求状态',
    size BIGINT COMMENT '返回文件的大小',
    referer STRING COMMENT '跳转来源',
    agent STRING COMMENT '浏览器UA'
    )
COMMENT 'ODS操作数据存储层'
PARTITIONED BY(dt STRING);

ALTER TABLE ods_log_tracker DROP IF EXISTS  PARTITION (dt='$bizdate$');
ALTER TABLE ods_log_tracker ADD PARTITION (dt='$bizdate$');

