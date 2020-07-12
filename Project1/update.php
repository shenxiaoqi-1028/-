<?php
require_once('dbinfo.php');

$id = $_POST['id'];

$name = $_POST['name'];
$comment = $_POST['comment'];


$tag = isset($_POST['tag'])? ($_POST['tag']==''?0:$_POST['tag']) :0;

$mydb = new mysqli($server_host,$user_name,$password,$db);

mysqli_connect_error()?die("数据库连接失败！"):'';
for($i=0;$i<count($tag);$i++){
  $sql = "SELECT tag_content,tag_id FROM tag WHERE tag_content='$tag[$i]'";
  $result=$mydb->query($sql);
  if(mysqli_num_rows($result)<=0){
  $tag_id = md5(uniqid());
  //insert_values($tag_id,$tag_content[$i]);
  $sql_a = "insert into tag values('$tag_id','$tag_content[$i]')";
  $result_a = $mydb->query($sql_a);

}
  else{
    $row = mysqli_fetch_assoc($result);
    $tag_id=$row['tag_id'];
  }
if($i==0){
  $sql = "update favorites set id = '$id', name = '$name' , comment = '$comment',tag_id='$tag_id'  where id = '$id' ";
  $result = $mydb->query($sql);
}
 else {
  $sql="insert into favorites values('$id','$name','$comment','$tag_id')";
   $result=$mydb->query($sql);
}
}




// $sql_a="update tag set tag_id ='$tag_id' where tag_content='$tag'";
// $result_x=$mydb->query($sql_a);

if($result){
    echo json_encode(array(
        "status"=> "success",
        "message"=>"数据更新成功！",
        "result"=>$result
    ));
}else{
    echo json_encode(array(
        "status"=> "fail",
        "message"=>$result,
        "sql"=>$sql
    ));
}

mysqli_close($mydb);

?>
