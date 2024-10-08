function changeImage() {
    //1.获取图片对象
    const img = document.querySelector('#myimage');
//2.判断图片的src属性,off时变为on, on时变为off
    if ( myimage.src.match("lightoff.gif")) {
        myimage.src = "lighton.gif";
    }
    else {
        myimage.src = "lightoff.gif";
    }
    
  }
