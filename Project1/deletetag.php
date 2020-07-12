<?php
require_once('dbinfo.php');

$id = isset($_POST['id'])?$_POST['id']:'';
$tag_id=isset($_POST['tag_id'])?$_POST['tag_id']:'';

$mydb = new mysqli($server_host,$user_name,$password,$db);

mysqli_connect_error()?die("数据库连接失败！"):'';


$tag_content='';
$sql="select tag_id from tag where tag_content='$tag_content'";
$result=$mydb->query($sql);
$row = mysqli_fetch_assoc($result);
$tag_idx=$row['tag_id'];


if($id ==''){
    echo "参数错误";
}else{
  $sql = "SELECT tag_id FROM favorites WHERE id='$id'";
  $result=$mydb->query($sql);
if(mysqli_num_rows($result)<=1){
  $sql= "update favorites set tag_id = '$tag_idx' where id = '$id'  ";}

  else{
    $sql = "DELETE from favorites where favorites.id='$id' and favorites.tag_id='$tag_id' ";//一条sql语句


    }
$result=$mydb->query($sql);
    if($result){
        echo json_encode(array(
            "status"=>"success",
            "message"=>"删除数据成功"
        ));
    }else{
        echo json_encode(array(
            "status"=>"fail",
            "message"=>"删除数据失败"
        ));
    }
//}
}


mysqli_close($mydb);
?>
