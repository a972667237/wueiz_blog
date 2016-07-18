$(document).ready(function(){
    $(".then").click(function(){
        var href = $(".article_all").eq(0).attr("href");
        $.getJSON("/ajax/more",{'href':href}, function(ret){
            var len = ret.length
            var i;
            if(ret[0].id < 4)
                $('.then').css('display','none')
            $('.pre').css('display','inline-block')
            for (i = 0; i < len; i++) {
              // 把 ret 的每一项显示在网页上
                $('.article_title').eq(i).html(ret[i].title);
                $('.article_content').eq(i).html(ret[i].content);
            };
            for(; i < 4; i++){
                $('.article_card').eq(i).css('display','none')
            };
        })
      });
    $('.pre').click(function(){
        var href = $(".article_all").eq(0).attr('href');
        $.getJSON('/ajax/pre',{'href':href},function(ret){
            var biggest = ret[0].biggest
            var i;
            for(i = 0; i < 4; i++){
                $('.article_card').eq(i).css('display','block')
            }
            if(biggest == ret[0].id)
                $('.pre').css('display','none')
            $('.then').css('display','inline-block')
            for (i = 0; i < 4; i++){
                $('.article_title').eq(i).html(ret[i].title);
                $('.article_content').eq(i).html(ret[i].content);
            }
        })
    })
});

