DROP TABLE IF EXISTS dm_kpi_info;

CREATE TABLE IF NOT EXISTS dm_kpi_info(
    time STRING COMMENT '日期',
    uv BIGINT COMMENT 'UV数',
    pv BIGINT COMMENT 'PV数',
    br BIGINT COMMENT '跳出率'
    )

INSERT OVERWRITE TABLE dm_kpi_info
SELECT
    t1.dt,
    count(distinct uid) as uv,
    count(t1.ip) as pv,
    brn/pv as br
FROM (
    SELECT
        #md5加密唯一性
        md5(concat(t1.ip, t1.device, t1.protocol, t1.identity, t1.agent)) as uid,
        t1.ip,
        case when count(t1.ip) ==1 then brn,
        t1.device,
        t1.protocol,
        t1.identity,
        t1.agent,
        t1.dt
    FROM
        (SELECT ip, protocol, agent, device, identity, dt
         FROM dw_weblog_info
         WHERE dt in ('20140101','20140102','20140103','20140104','20140105','20140106')
         GROUP BY ip, protocol, agent, device, identity,dt
        ) t1
    ）