<?php
require_once('dbinfo.php');

$id = isset($_POST['id'])?$_POST['id']:'';
$tag_id=isset($_POST['tag_id'])?$_POST['tag_id']:'';

$mydb = new mysqli($server_host,$user_name,$password,$db);

mysqli_connect_error()?die("数据库连接失败！"):'';
$comment='';
if($id ==''){
    echo "参数错误";
}else{
    $sql = "update favorites set  comment = '$comment' where id = '$id'  ";//一条sql语句


    $result = $mydb->query($sql);

    if($result){
        echo json_encode(array(
            "status"=>"success",
            "message"=>"删除评论成功"
        ));
    }else{
        echo json_encode(array(
            "status"=>"fail",
            "message"=>"删除评论失败"
        ));
    }
}


mysqli_close($mydb);
?>
