(function (jq) {

    /*
     Asc排序
     end:数组长度
     args:要排序的数组，例：[{'key':11,'value':'Usa'},{'key':21,'value':'China']
     */
    function SortAsc(end, args) {
        if (end <= 0) {
            return args;
        } else if (end == 1) {
            return args;
        } else {
            var bigerIndex = end - 1;
            for (i = 0; i < end - 1; i++) {
                if (args[i].value > args[bigerIndex].value) {
                    bigerIndex = i;
                }
            }
            var temp = args[bigerIndex];
            args[bigerIndex] = args[end - 1];
            args[end - 1] = temp;
            return SortAsc(end - 1, args);
        }
    }

    /*
     Desc排序
     end:数组长度
     args:要排序的数组，例：[{'key':11,'value':'Usa'},{'key':21,'value':'China']
     */
    function SortDesc(end, args) {
        if (end <= 0) {
            return args;
        } else if (end == 1) {
            return args;
        } else {
            var smallerIndex = end - 1;
            for (i = 0; i < end - 1; i++) {
                if (args[i].value < args[smallerIndex].value) {
                    smallerIndex = i;
                }
            }
            var temp = args[smallerIndex];
            args[smallerIndex] = args[end - 1];
            args[end - 1] = temp;
            return SortDesc(end - 1, args);
        }
    }

    function DoTrIntoEdit($tr, specialInEditFunc) {
        $tr.find('td[edit-enable="true"]').each(function () {
            ExecuteTdIntoEdit($(this), specialInEditFunc);
        });
    }

    function DoTrOutEdit($tr, specialOutEditFunc) {
        $tr.find('td[edit-enable="true"]').each(function () {
            ExecuteTdOutEdit($(this), specialOutEditFunc);
        });
    }

    function ExecuteTdIntoEdit($td, specialInEditFunc) {
        var editType = $td.attr('edit-type');

        if (editType == 'input') {
            var text = $td.text();
            $td.addClass('padding-3');
            var htmlTag = $.CreateInput({'value': text, 'class': 'padding-tb-5 form-control '}, {'width': '100%'});
            $td.empty().append(htmlTag);
        } else if (editType == 'select') {
            var globalName = $td.attr('global-name');
            var selectedId = $td.attr('id');
            if (specialInEditFunc) {
                specialInEditFunc($td, globalName, selectedId);
            } else {
                $td.addClass('padding-3');
                var htmlTag = $.CreateSelect(
                    {'class': 'padding-tb-5 form-control'},
                    {'width': '100%'},
                    window[globalName],
                    selectedId,
                    'id',
                    'name'
                );
                $td.empty().append(htmlTag);
            }
        }

    }

    function ExecuteTdOutEdit($td, specialOutEditFunc) {
        var editType = $td.attr('edit-type');

        if (editType == 'input') {
            var text = $td.children().first().val();
            $td.removeClass('padding-3');
            $td.empty().text(text);
        } else if (editType == 'select') {
            var globalName = $td.attr('global-name');

            if (specialOutEditFunc) {
                specialOutEditFunc($td, globalName);
            }
            else {
                $td.removeClass('padding-3');
                var selecting_val = $td.children().first().val();
                var selecting_text = $td.children().first().find("option[value='" + selecting_val + "']").text();
                $td.empty().html(selecting_text);
                $td.attr('id', selecting_val);
            }
        }
    }

    jq.extend({
        'initMenu': function (target) {
            $(target).addClass('active').siblings().removeClass('active');
        },
        'CreateTd': function (attrs, csses, text) {
            var obj = document.createElement('td');
            $.each(attrs, function (k, v) {
                $(obj).attr(k, v);
            });
            $.each(csses, function (k, v) {
                $(obj).css(k, v);
            });
            $(obj).html(text);
            return obj;
        },
        'CreateTds': function (attrs, csses, list, seprate) {
            var obj = document.createElement('td');
            $.each(attrs, function (k, v) {
                $(obj).attr(k, v);
            });
            $.each(csses, function (k, v) {
                $(obj).css(k, v);
            });
            $.each(list, function (k, v) {
                if (k == 0) {
                    $(obj).append(v);
                } else {
                    $(obj).append(seprate);
                    $(obj).append(v);
                }
            });
            return obj;
        },
        'CreateTr': function (attrs, csses, tds) {
            var obj = document.createElement('tr');
            $.each(attrs, function (k, v) {
                $(obj).attr(k, v);
            });
            $.each(csses, function (k, v) {
                $(obj).css(k, v);
            });
            $.each(tds, function (k, v) {
                $(v).appendTo($(obj));
            });
            return obj;
        },
        'CreateInput': function (attrs, csses) {
            var obj = document.createElement('input');
            $.each(attrs, function (k, v) {
                $(obj).attr(k, v);
            });
            $.each(csses, function (k, v) {
                $(obj).css(k, v);
            });
            return obj
        },
        'CreateA': function (attrs, csses, text) {
            var obj = document.createElement('a');
            $.each(attrs, function (k, v) {
                $(obj).attr(k, v);
            });
            $.each(csses, function (k, v) {
                $(obj).css(k, v);
            });
            $(obj).html(text);
            return obj
        },
        'CreateOption': function (attrs, csses, text) {
            var obj = document.createElement('option');
            $.each(attrs, function (k, v) {
                $(obj).attr(k, v);
            });
            $.each(csses, function (k, v) {
                $(obj).css(k, v);
            });
            $(obj).html(text);
            return obj
        },

        /*
         创建Select标签
         options: 必须是含有id和name的对象，id作为option的value，name作为option的内容，例：obj.id = 1,obj.name = 'China'
         current: 当前被选中的内容，例：current ＝ 'China'
         key_value,key_text是全局字典的key和value的key
         */
        'CreateSelect': function (attrs, csses, option_data_list, current_value, key_value, key_text) {
            var sel = document.createElement('select');
            $.each(attrs, function (k, v) {
                $(sel).attr(k, v);
            });
            $.each(csses, function (k, v) {
                $(sel).css(k, v);
            });
            $.each(option_data_list, function (k, v) {
                var opt1 = document.createElement('option');
                var sel_text = v[key_text];
                var sel_value = v[key_value];
                if (sel_value == current_value) {
                    $(opt1).text(sel_text).attr('value', sel_value).attr('text', sel_text).appendTo($(sel));
                    $(opt1).prop('selected', true);
                } else {
                    $(opt1).text(sel_text).attr('value', sel_value).attr('text', sel_text).appendTo($(sel));
                }
            });
            return sel;
        },


        /*
         搜索插件 -> 添加搜索条件
         ths:点击的当前对象
         */
        'AddSearchCondition': function (ths) {
            var $duplicate = $(ths).parent().parent().clone(true);
            $duplicate.find('.fa-plus-square').addClass('fa-minus-square').removeClass('fa-plus-square');
            $duplicate.find('a[onclick="$.AddSearchCondition(this)"]').attr('onclick', "$.RemoveSearchCondition(this)");

            $duplicate.appendTo($(ths).parent().parent().parent());
        },

        /*
         搜索插件 -> 移除当前搜索条件
         ths:点击的当前对象
         */
        'RemoveSearchCondition': function (ths) {
            $(ths).parent().parent().remove();
        },

        'Hide': function (target) {
            $(target).addClass('hide');
        },

        'Show': function (target) {
            $(target).removeClass('hide');
        },
        /*
         表格CheckBox全选
         tableBody:表格中body选择器对象
         rowEditFunc:行进入编辑模式的特殊函数处理，例如：状态、等不同的样式
         */
        'CheckAll': function (tableBody, specialInEditFunc) {

            if ($(tableBody).attr('edit-mode') == 'true') {
                $(tableBody).find(':checkbox').each(function () {
                    var check = $(this).prop('checked');
                    var disabled = $(this).prop('disabled');
                    var $tr = $(this).parent().parent();
                    if (!check && !disabled) {
                        $tr.addClass('success');
                        $(this).prop('checked', true);
                        DoTrIntoEdit($tr, specialInEditFunc);
                    }
                });
            } else {
                $(tableBody).find(':checkbox').each(function () {
                    var disabled = $(this).prop('disabled');
                    if (!disabled) {
                        $(this).prop('checked', true);
                    }
                });
            }
            //$(tableBody).find(':checkbox').prop('checked',true);
        },

        /*
         表格CheckBox取消选择
         tableBody:表格中body选择器对象
         */
        'UnCheckAll': function (tableBody, specialOutEditFunc) {


            if ($(tableBody).attr('edit-mode') == 'true') {
                $(tableBody).find(':checkbox').each(function () {
                    var check = $(this).prop('checked');
                    var $tr = $(this).parent().parent();
                    if (check) {
                        $tr.removeClass('success');
                        DoTrOutEdit($tr, specialOutEditFunc);
                    }
                });
            }

            $(tableBody).find(':checkbox').prop('checked', false);
        },

        /*
         表格CheckBox反选
         targetContainer:表格中body选择器对象
         specialInEditFunc:
         specialOutEditFunc:
         */
        'ReverseCheck': function (tableBody, specialInEditFunc, specialOutEditFunc) {
            $(tableBody).find(':checkbox').each(function () {
                var check = $(this).prop('checked');
                var disabled = $(this).prop('disabled');
                var $tr = $(this).parent().parent();
                if (check) {
                    $(this).prop('checked', false);
                    if ($(tableBody).attr('edit-mode') == 'true') {
                        $tr.removeClass('success');
                        DoTrOutEdit($tr, specialOutEditFunc);
                    }
                } else {
                    if (!disabled) {
                        $(this).prop('checked', true);
                    }
                    if ($(tableBody).attr('edit-mode') == 'true' && !disabled) {
                        $tr.addClass('success');
                        //this row enable edit
                        DoTrIntoEdit($tr, specialInEditFunc);
                    }

                }
            })
        },

        /*
         绑定点击CheckBox事件
         targetContainer:表格中body选择器对象
         specialInEditFunc:
         specialOutEditFunc:
         */
        'BindDoSingleCheck': function (tableBody, specialInEditFunc, specialOutEditFun) {
            $(tableBody).delegate(':checkbox','click', function () {
                var $tr = $(this).parent().parent();
                if ($(this).prop('checked')) {
                    if ($(tableBody).attr('edit-mode') == 'true') {
                        //this row switch in edit mode
                        $tr.addClass('success');
                        DoTrIntoEdit($tr, specialInEditFunc);
                    }
                } else {
                    if ($(tableBody).attr('edit-mode') == 'true') {
                        //this row switch out edit mode
                        $tr.removeClass('success');
                        DoTrOutEdit($tr, specialOutEditFun);
                    }
                }

            });
        },

        /*
         表格排序
         header:表格中header选择器对象
         body:表格中body选择器对象
         */
        'BindTableSort': function (header, body) {
            $(header).find("th[en-sort='true']").unbind('click');
            $(header).find("th[en-sort='true']").bind('click', function () {

                var currentIndex = $(this).index();
                var originList = [];
                var keyValueList = [];
                $(body).children().each(function (k, v) {
                    originList.push($(v));
                    var currentData = $(this).children().eq(currentIndex).text();
                    keyValueList.push({'key': k, 'value': currentData});
                });

                if ($(this).hasClass('both')) {
                    //Asc排序
                    $(this).removeClass('both').addClass('desc').siblings().removeClass('asc desc').addClass('both');
                    var sorted = SortDesc(keyValueList.length, keyValueList);
                } else if ($(this).hasClass('desc')) {
                    //Desc排序
                    $(this).removeClass('desc').addClass('asc').siblings().removeClass('asc desc').addClass('both');
                    var sorted = SortAsc(keyValueList.length, keyValueList);
                } else if ($(this).hasClass('asc')) {
                    //Asc排序
                    $(this).removeClass('asc').addClass('desc').siblings().removeClass('asc desc').addClass('both');
                    var sorted = SortDesc(keyValueList.length, keyValueList);
                }
                if (sorted) {
                    $(body).empty();
                    $.each(sorted, function (k, v) {
                        $(body).append(originList[v.key]);
                    });
                    $.BindDoSingleCheck(body);
                }

            })
        },
        /*
         重置排序
         */
        'ResetTableSort': function (header, body) {
            $(header).find("th[en-sort='true']").removeClass('desc asc').addClass('both');
        },

        /*
         表格进入编辑模式
         ths:当前点击的按钮
         body:表格中body选择器对象
         */
        'TableEditMode': function (ths, body, specialInEditFunc, specialOutEditFunc) {
            if ($(ths).hasClass('btn-warning')) {
                $(ths).removeClass('btn-warning').find('span').text('进入编辑模式');

                $(body).attr('edit-mode', 'false');

                $(body).children().removeClass('success');

                $(body).find(':checkbox').each(function () {
                    var check = $(this).prop('checked');
                    var $tr = $(this).parent().parent();
                    if (check) {
                        $tr.removeClass('success');
                        DoTrOutEdit($tr, specialOutEditFunc);
                    }
                });

            } else {
                //into edit mode
                $(ths).addClass('btn-warning').find('span').text('退出编辑模式');
                $(body).attr('edit-mode', 'true');

                $(body).find(':checkbox').each(function () {
                    var check = $(this).prop('checked');
                    var $tr = $(this).parent().parent();
                    if (check) {
                        $tr.addClass('success');
                        DoTrIntoEdit($tr, specialInEditFunc);
                    }
                });
            }
        },

        /*
         tab菜单(例如：$.BindTabMenu('#tab-menu-title', '#tab-menu-body');)
         */
        'BindTabMenu': function (title, body) {
            $(title).children().bind("click", function () {
                var $menu = $(this);
                var $content = $(body).find('div[content="' + $(this).attr("content-to") + '"]');
                $menu.addClass('current').siblings().removeClass('current');
                $content.removeClass('hide').siblings().addClass('hide');
            });
        }
    });
})(jQuery);