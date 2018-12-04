/*默认查询时间*/
function DefaultTime(starttime, days) {
    //日期的默认值
    var now = new Date(),
        past = new Date();
    var begin = starttime ? starttime : 2,
        days = days ? days : 8;
    now.setDate(now.getDate() - begin);
    past.setDate(past.getDate() - days);

    var nowyear = now.getFullYear(),
        nowMonth = now.getMonth() < 9 ? '0'+ (now.getMonth() + 1) : now.getMonth() + 1,
        nowDay = now.getDate() < 10 ? '0'+ now.getDate() : now.getDate();
    var pastyear = past.getFullYear(),
        pastMonth = past.getMonth() < 9 ? '0'+ (past.getMonth() + 1) : past.getMonth() + 1,
        pastDay = past.getDate() < 10 ? '0'+ past.getDate() : past.getDate();
    var starttime = pastyear + '-'+ pastMonth + '-'+ pastDay;
    var endtime = nowyear + '-'+ nowMonth + '-'+ nowDay;
    return [starttime, endtime];
}
/*引擎名字转换*/
var rpList = {
    'didi':'拼车一致性',
    'multiroute':'V3',
    'rp':'V2',
    'soso':'腾讯'
}
/*城市英文转中文的数据库*/
var uniqueCityList = {
    'beijing': '北京',
    'changchun':'长春',
    'changsha':'长沙',
    'changzhou':'常州',
    'chengdu':'成都',
    'chongqing':'重庆',
    'dalian':'大连',
    'dongguan':'东莞',
    'foshan':'佛山',
    'fuzhou':'福州',
    'guangzhou':'广州',
    'haerbin':'哈尔滨',
    'hangzhou':'杭州',
    'hefei':'合肥',
    'huizhou':'惠州',
    'huzhou':'湖州',
    'jiaxing':'嘉兴',
    'jinan':'济南',
    'jinhua':'金华',
    'kunming':'昆明',
    'nanchang':'南昌',
    'nanjing':'南京',
    'nanning':'南宁',
    'ningbo':'宁波',
    'qingdao':'青岛',
    'quanzhou':'泉州',
    'shanghai':'上海',
    'shaoxing':'绍兴',
    'shenyang':'沈阳',
    'shenzhen':'深圳',
    'shijiazhuang':'石家庄',
    'suzhou':'苏州',
    'taiyuan':'太原',
    'tianjin':'天津',
    'wenzhou':'温州',
    'wuhan':'武汉',
    'wuxi':'无锡',
    'xiamen':'厦门',
    'xian':'西安',
    'yantai':'烟台',
    'zhengzhou':'郑州',
    'zhongshan':'中山',
    'zhuhai':'珠海',
}