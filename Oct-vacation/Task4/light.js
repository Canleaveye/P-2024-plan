function changeImage() {
    //1.获取图片对象
    const img = document.querySelector('#myimage');
//2.判断图片的src属性,off时变为on, on时变为off
    if ( myimage.src.match("./resources/imgs/pic_bulboff.gif")) {
        myimage.src = "./resources/imgs/pic_bulbon.gif";
    }
    else {
        myimage.src = "./resources/imgs/pic_bulboff.gif";
    }
    
  }
