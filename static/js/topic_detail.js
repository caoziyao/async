
$(document).ready(function(){
    var log = function(){
        console.log(arguments)
    }

    var editor = new wangEditor('wangEditor-comment')


        // 配置 onchange 事件
    // editor.onchange = function () {
    //     // 编辑区域内容变化时，实时打印出当前内容
    //     log(this.$txt.html());
    // };
    editor.create()


    var bindEventCommentAdd = function(){

    }

    var commentTemplate = function(commnet){
        var c = commnet
        var date = c.created_time
        
        var t = `
            <div class="cell clearfix">
                <div class="item-img">
                    <img class="avatar"  src="${ c.user_img_url }" alt="头像">
                </div>
                
                <div class="item-content">
                    <div>
                        ${ c.username } at  <stamp>${ dateDiff(date) }</stamp>
                    </div>
                        <div class="jq-commet">
                            ${ c.comment }
                        </div>
                </div>
            </div>
        `
        return t
    }


    $('#id-button-comment-add').click(function () {
        // 获取编辑器区域完整html代码
        var html = editor.$txt.html();
        var user_id = $('#id-button-user-id').attr("value")
        var topic_id = $('#id-button-topic-id').attr("value")
        // log(topic_id)
        var form = {
            comment: html,
            user_id: user_id,
            topic_id: topic_id,
        }

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
          log('成功', arguments)
          if(r.success){
            //   log('r', r.comment)
            c = r.data
            $('.comments').prepend(commentTemplate(c))
            log('添加成功')
          }
          else{
              log('添加失败')
          }
        }

      // 把上面的 form 和 response 函数传给 weiboAdd
      // api 在 api.js 中，因为页面会先引用 api.js 再引用 weibo.js
      // 所以 weibo.js 里面可以使用 api.js 中的内容
      api.commentAdd(form, response)


    })



})
