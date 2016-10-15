
$(document).ready(function(){
    var log = function(){
        console.log(arguments)
    }

    var editor = new wangEditor('wang-topic')


        // 配置 onchange 事件
    // editor.onchange = function () {
    //     // 编辑区域内容变化时，实时打印出当前内容
    //     log(this.$txt.html());
    // };
    editor.create()



 $('#id-button-topic-add').click(function () {
        // 获取编辑器区域完整html代码
        var html = editor.$txt.html();
        var note_id = $('#id-button-option-value').val()
        var title = $('#id-button-title').val()
        
        // log(note_id)
        var form = {
            content: html,
            title: title,
            note_id: note_id,
        }

        // log(form)

        // 这个响应函数会在 AJAX 调用完成后被调用
        var response = function(r){
          /*
          这个函数会被 commentAdd 调用，并且传一个 r 参数进来
          r 参数的结构如下
          {
              'success': 布尔值,
              'data': 数据,
              'message': 错误消息
          }
          */
          // arguments 是包含所有参数的一个 list
        //   log('成功', arguments)
          if(r.success){
            //   log('r', r.comment)
            // log('添加成功')
            node_id = r.data.node_id
            // log(node_id)
            alert('发布成功, 正在为你跳转...')
            location.href = "/topic/?node_id=" + node_id;//location.href实现客户端页面的跳转
          }
          else{
            //   log('添加失败')
              alert('网络错误...')
          }
        }

      // 把上面的 form 和 response 函数传给 weiboAdd
      // api 在 api.js 中，因为页面会先引用 api.js 再引用 weibo.js
      // 所以 weibo.js 里面可以使用 api.js 中的内容
    //   api.commentAdd(form, response)

        api.topicAdd(form, response)
    })






})
