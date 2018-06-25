/**
 * Created by wupeiqi on 17/2/24.
 */
function nbDataList(requestUrl) {

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
            }
        }
    });

    initialize(1);
    bindMenuFunction();
    bindMultiSelect();
    bindSearchCondition();


    function saveData() {
        // 退出编辑模式
        if ($('#edit_mode_target').hasClass('btn-warning')) {
            $.TableEditMode('#edit_mode_target', '#table_body', null, null);
        }

        // 获取被修改过的数据
        var updateData = [];
        $('#table_body').children().each(function () {
            var rows = {};
            var nid = $(this).attr('nid');
            var num = $(this).attr('num');

            var flag = false;
            $(this).children('td[edit-enable="true"]').each(function () {
                var original = $(this).attr('original');
                var name = $(this).attr('name');
                var newer;
                if ($(this).attr('edit-type') == 'input') {
                    newer = $(this).text();

                } else if ($(this).attr('edit-type') == 'select') {
                    newer = $(this).attr('id');
                }
                if (newer != undefined && original != newer) {
                    rows[name] = newer;
                    flag = true;
                }
            });
            if (flag) {
                rows["nid"] = nid;
                rows["num"] = num;
                updateData.push(rows);
            }
        });
        if (updateData.length < 1) {
            return;
        }
        updateData = JSON.stringify(updateData);

        $.ajax({
            url: requestUrl,
            type: 'PUT',
            data: {update_list: updateData},
            success: function (response) {
                if (response.status) {
                    SuccessHandleStatus(response.message);
                } else {
                    ErrorHandleStatus(response.message, response.error);
                }
                refreshData();

            },
            error: function () {
                alert('请求异常');
            }
        })
    }

    function refreshData() {
        var currentPage = $('#pager').find("li[class='active']").text();
        initialize(currentPage);
    }

    function deleteData() {
        var id_list = [];
        $('#table_body').find(':checkbox').each(function () {
            if ($(this).prop('checked')) {
                id_list.push($(this).val());
            }
        });
        $.ajax({
            url: requestUrl,
            type: 'DELETE',
            data: {id_list: id_list},
            traditional: true,
            success: function (response) {
                if (response.status) {
                    SuccessHandleStatus(response.message);
                } else {
                    alert(response.message);
                }
                refreshData();

            },
            error: function () {
                alert('请求异常');
            }
        })
    }

    /*
     绑定头部按钮事件
     */
    function bindMenuFunction() {
        $('#edit_mode_target').click(function () {
            $.TableEditMode(this, '#table_body', null, null)
        });

        $('#check_all').click(function () {
            $.CheckAll('#table_body', null);
        });

        $('#check_cancel').click(function () {
            $.UnCheckAll('#table_body', null);
        });

        $('#check_reverse').click(function () {
            $.ReverseCheck('#table_body', null, null)
        });

        $('#do_delete').click(function () {
            $.Show('#shade,#modal_delete');
        });
        $('#do_delete_confirm').click(function () {
            deleteData();
        });

        $('#do_save').click(function () {
            saveData();
        });

        $('#do_refresh').click(function () {
            refreshData();
        });

    }

    /*
     绑定搜索条件的事件
     */
    function bindSearchCondition() {
        bindChangeSearchCondition();
        bindSubmitSearchCondition();
    }

    /*
     聚合搜索条件
     */
    function aggregationSearchCondition() {
        var ret = {};
        $("#search_conditions").children().each(function () {
            var $condition = $(this).find("input[is-condition='true'],select[is-condition='true']");
            var name = $condition.attr('name');
            var value = $condition.val();
            if (!$condition.is('select')) {
                name = name + "__contains";
            }
            if (value) {
                var valList = $condition.val().trim().replace('，', ',').split(',');
                if (ret[name]) {
                    ret[name] = ret[name].concat(valList);
                } else {
                    ret[name] = valList;
                }
            }
        });
        return ret;
    }

    /*
     页面初始化（获取数据，绑定事件）
     */
    function initialize(pager) {
        $.Show('#shade,#loading');
        var conditions = JSON.stringify(aggregationSearchCondition());
        var $body = $('#table_body');
        $.ajax({
            url: requestUrl,
            type: 'GET',
            traditional: true,
            data: {'condition': conditions, 'pager': pager},
            dataType: 'JSON',
            success: function (response) {
                $.Hide('#shade,#loading');
                if (response.status) {
                    initGlobal(response.data.global_dict);
                    initTableHeader(response.data.table_config);
                    initTableBody(response.data.page_info.page_start, response.data.data_list, response.data.table_config);
                    initPager(response.data.page_info.page_str);
                    initSearchCondition(response.data.condition_config);
                    $.BindDoSingleCheck('#table_body', null, null);
                } else {
                    alert(response.message);
                }
            },
            error: function () {
                $.Hide('#shade,#loading');
            }
        })

    }

    /*
     初始化全局变量
     */
    function initGlobal(globalDict) {
        $.each(globalDict, function (k, v) {
            window[k] = v;
        })
    }

    /*
     初始化表格的头部
     */
    function initTableHeader(tbConfig) {
        var $header = $('#table_head');

        $header.find('th').remove();

        // 创建“选择列”
        var ck = document.createElement('th');
        ck.innerText = '选择';
        $header.find('tr').append(ck);

        // 创建“序号列”
        var num = document.createElement('th');
        num.innerText = '序号';
        $header.find('tr').append(num);


        $.each(tbConfig, function (k, item) {
            if (item.display) {
                var tag = document.createElement('th');
                tag.innerText = item.title;
                $header.find('tr').append(tag);
            }

        });
    }

    /*
     初始化表格内容
     */
    function initTableBody(startNum, list, tbConfig) {
        var $body = $('#table_body');
        $body.empty();

        $.each(list, function (k1, row) {
            var tr = document.createElement('tr');
            tr.setAttribute('nid', row['id']);
            tr.setAttribute('num', startNum + k1 + 1);
            // 创建每一行的CheckBox
            var tagTd = document.createElement('td');
            var tagCheckBox = document.createElement('input');
            tagCheckBox.type = 'checkbox';
            tagCheckBox.value = row['id'];
            $(tagTd).append(tagCheckBox);
            $(tr).append(tagTd);
            // 创建每一行的CheckBox
            var tagNum = document.createElement('td');
            tagNum.innerHTML = startNum + k1 + 1;
            $(tr).append(tagNum);

            $.each(tbConfig, function (k2, config) {
                var td = document.createElement('td');
                if (config.display == 1) {
                    td.innerText = row[config.q];
                    td.setAttribute('original', row[config.q]);
                    $.each(config.attr, function (attr_key, attr_value) {
                        if (attr_value.startsWith('@')) {
                            td.setAttribute(attr_key, row[attr_value.substring(1, attr_value.lenght)]);
                            td.setAttribute('original', row[attr_value.substring(1, attr_value.lenght)]);
                        } else {
                            td.setAttribute(attr_key, attr_value);
                        }
                    });
                    $(tr).append(td);
                } else if (config.display == 2) {
                    $.each(config.attr, function (attr_key, attr_value) {
                        if (attr_value.startsWith('@@')) {
                            var global_name = attr_value.substring(2, attr_value.length);
                            td.innerText = getNameByGlobalList(global_name, row[config.q]);
                            td.setAttribute(attr_key, row[config.q]);
                            td.setAttribute('original', row[config.q]);
                        } else {
                            td.setAttribute(attr_key, attr_value);
                        }
                    });
                    $(tr).append(td);
                }
            });
            $body.append(tr);
        })
    }

    /*
     根据ID从全局变量中获取其对应的内容
     */
    function getNameByGlobalList(globalName, itemId) {
        var result;
        $.each(window[globalName], function (k, v) {
            if (v.id == itemId) {
                result = v.name;
                return false;
            }
        });
        return result;
    }

    /*
     初始化分页内容
     */
    function initPager(pageStr) {
        var $pager = $('#pager');
        $pager.empty();
        $pager.append(pageStr);
    }

    /*
     初始化搜索条件
     */
    function initSearchCondition(config) {
        var $search_condition = $('#search_condition');
        if ($search_condition.attr('init') == 'true') {
            return
        }
        if (config.length > 0) {
            var first_item = config[0];
            initDefaultSearchCondition(first_item);
        }

        $.each(config, function (k, v) {
            var condition_type = v['condition_type'];
            var tag = document.createElement('li');
            var a = document.createElement('a');
            a.innerHTML = v['text'];
            $(tag).append(a);
            tag.setAttribute('name', v['name']);
            tag.setAttribute('condition-type', condition_type);
            if (condition_type == 'select') {
                tag.setAttribute('global-name', v['global_name']);
            }
            $('#search_condition').find('ul').append(tag);
        });
        $search_condition.attr('init', 'true');
    }

    /*
     初始化默认的第一个条件
     */
    function initDefaultSearchCondition(item) {

        var tag;
        if (item.condition_type == 'input') {
            tag = $.CreateInput({
                'is-condition': 'true',
                'class': 'form-control no-radius',
                'name': item.name,
                'placeholder': '逗号分割多条件'
            }, {});
        } else if (item.condition_type == 'select') {
            tag = $.CreateSelect({
                'is-condition': 'true',
                'class': 'form-control select-icon no-radius',
                'name': item.name
            }, {}, window[item.global_name], null, 'id', 'name');
        }
        var $current = $('#search_condition');
        $current.children().first().text(item.text);
        $current.after(tag);

    }

    /*
     绑定修改条件之后的事件
     */
    function bindChangeSearchCondition() {
        $('#search_condition').find('ul').delegate('li', 'click', function () {
            var name = $(this).attr('name');
            var text = $(this).text();
            var condition_type = $(this).attr('condition-type');
            var global_name = $(this).attr('global-name');
            var tag;
            if (condition_type == 'input') {
                tag = $.CreateInput({
                    'is-condition': 'true',
                    'class': 'form-control no-radius',
                    'name': name,
                    'placeholder': '逗号分割多条件'
                }, {});
            } else if (condition_type == 'select') {
                tag = $.CreateSelect({
                    'is-condition': 'true',
                    'class': 'form-control select-icon no-radius',
                    'name': name
                }, {}, window[global_name], null, 'id', 'name');
            }
            var $current = $(this).parent().parent();
            $current.children().first().text(text);
            $current.next().remove();
            $current.after(tag);

        });
    }

    /*
     绑定提交搜索按钮
     */
    function bindSubmitSearchCondition() {
        $('#search_condition_submit').click(function () {
            initialize(1);
        });
    }

    /*
     更新资产错误，显示错误信息
     */
    function ErrorHandleStatus(content, errorList) {
        var $handle_status = $('#handle_status');
        $handle_status.attr('data-toggle', 'popover');

        var errorStr = '';
        $.each(errorList, function (k, v) {
            errorStr = errorStr + v.num + '. ' + v.message + '</br>';
        });

        $handle_status.attr('data-content', errorStr);
        $handle_status.popover();

        var msg = "<i class='fa fa-info-circle'></i>" + content;
        $handle_status.empty().removeClass('btn-success').addClass('btn-danger').html(msg);

    }

    /*
     更新资产成功，显示更新信息
     */
    function SuccessHandleStatus(content) {
        var $handle_status = $('#handle_status');
        $handle_status.popover('destroy');
        var msg = "<i class='fa fa-check'></i>" + content;
        $handle_status.empty().removeClass('btn-danger').addClass('btn-success').html(msg);
        setTimeout(function () {
            $handle_status.empty().removeClass('btn-success btn-danger');
        }, 5000);
    }

    /*
     监听是否已经按下control键
     */
    window.globalCtrlKeyPress = false;
    window.onkeydown = function (event) {
        if (event && event.keyCode == 17) {
            window.globalCtrlKeyPress = true;
        }
    };

    window.onkeyup = function (event) {
        if (event && event.keyCode == 17) {
            window.globalCtrlKeyPress = false;
        }
    };

    /*
     按下Control，联动表格中正在编辑的select
     */
    function bindMultiSelect() {
        $('#table_body').delegate('select', 'change', function () {
            if (window.globalCtrlKeyPress) {
                var index = $(this).parent().index();
                var value = $(this).val();
                $(this).parent().parent().nextAll().find("td input[type='checkbox']:checked").each(function () {
                    $(this).parent().parent().children().eq(index).children().val(value);
                });
            }
        });

    }

}