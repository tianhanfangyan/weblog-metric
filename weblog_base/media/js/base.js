$(document).ready(function() {
    var url = window.location.href;
    var urlArr = url.split('/'),
         length = urlArr.length;
    var  idPage = urlArr[length-1],
         idSection = urlArr[length-2];
    $("#"+idPage ).addClass("selected");    
    $("#"+idSection ).addClass("show");
})


// Dropdown Menu
var dropdown = document.querySelectorAll('.dropdown-new');
var dropdownArray = Array.prototype.slice.call(dropdown, 0);
dropdownArray.forEach(function(el) {
    var button = el.querySelector('a[data-toggle="dropdown-new"]'),
        menu = el.querySelector('.dropdown-new-menu'),
        arrow = button.querySelector('i.arrow');

    button.onclick = function(event) {
        if (!menu.hasClass('show')) {
            menu.classList.add('show');
            menu.classList.remove('hide');
            arrow.classList.add('open');
            arrow.classList.remove('icon-arrow-down');
            event.preventDefault();
        } else {
            menu.classList.remove('show');
            menu.classList.add('hide');
            arrow.classList.remove('open');
            arrow.classList.add('icon-arrow-down');
            event.preventDefault();
        }
    };
})
Element.prototype.hasClass = function(className) {
    return this.className && new RegExp("(^|\\s)" + className + "(\\s|$)").test(this.className);
};

//全屏启动
function launchFullScreen(element) {
    element.style.width = '1000px';
    element.style.height = '600px';
    if (element.requestFullscreen) {
        element.requestFullscreen();
    } else if (element.mozRequestFullScreen) {
        element.mozRequestFullScreen();
    } else if (element.webkitRequestFullscreen) {
        element.webkitRequestFullscreen();
    } else if (element.msRequestFullscreen) {
        element.msRequestFullscreen();
    }


}
//全屏关闭
function exitFullScreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
    } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
    }
}


/*JSON转为CSV文件*/
function JSONintoCSV(fileName, JSONData) {
    var arrData = typeof JSONData !== 'object' ? JSON.parse(JSONData) : JSONData;
    var CSV = '',
        row = '';
    //取得字段名字
    for (var index in arrData[0]) {
        row += index + ',';
    }
    row = row.slice(0, -1);
    CSV += row + '\r\n';
    //取得数据
    for (var i = 0; i < arrData.length; i++) {
        var row = "";
        for (var index in arrData[i]) {
            var arrValue = arrData[i][index] == null ? "" : '="' + arrData[i][index] + '"';
            row += arrValue + ',';
        }
        row.slice(0, row.length - 1);
        CSV += row + '\r\n';
    }
    if (CSV == '') {
        growl.error("Invalid data");
        return;
    }
    //非ie浏览器的转化
    var uri = 'data:text/csv;charset=utf-8,\uFEFF' + encodeURI(CSV);
   // var uri = 'data:application/csv;charset=utf-8,' + escape(CSV);
    var link = document.createElement("a");
    link.href = uri;
    link.style = "visibility:hidden";
    link.download = fileName + ".csv";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

/*数组转为CSV文件*/
function ArrayintoCSV(fileName, ArrData) {
    var CSV = '',
        row = '';
    //取得字段名字
    for (index in ArrData) {
        row += index + ',';
    }
    row = row.slice(0, -1);
    CSV += row + '\r\n';
    //取得数据
    for (var i = 0; i < arrData.length; i++) {
        var row = "";
        for (var index in arrData[i]) {
            var arrValue = arrData[i][index] == null ? "" : '="' + arrData[i][index] + '"';
            row += arrValue + ',';
        }
        row.slice(0, row.length - 1);
        CSV += row + '\r\n';
    }
    if (CSV == '') {
        growl.error("Invalid data");
        return;
    }
    //非ie浏览器的转化
    var uri = 'data:application/csv;charset=utf-8,' + escape(CSV);
    var link = document.createElement("a");
    link.href = uri;
    link.style = "visibility:hidden";
    link.download = fileName + ".csv";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}