

<?php
require_once('dbinfo.php');
// ini_set("display_errors","On");
// error_reporting(E_ALL);



$id = md5(uniqid());

$name = $_POST['name'];
$comment = $_POST['comment'];
$tag_content = isset($_POST['tag'])? ($_POST['tag']==''?0:$_POST['tag']) :0;

$mydb = new mysqli($server_host,$user_name,$password,$db);

mysqli_connect_error()?die("数据库连接失败！"):'';




for($i=0;$i<count($tag_content);$i++){

  $sql = "SELECT tag_content,tag_id FROM tag WHERE tag_content='$tag_content[$i]'";
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


$sql="insert into favorites_tag_relation values('$id','$tag_id')";
$result=$mydb->query($sql);
$sql_b = "insert into favorites values('$id','$name','$comment','$tag_id')";
$result_b = $mydb->query($sql_b);

}

if($result_b){
    echo json_encode(array(
        "status"=> "success",
        "message"=>"数据写入成功！"
    ));
}else{
    echo json_encode(array(
        "status"=> "fail",
        "message"=> $result_b,
        "sql"=> $sql_b
    ));
}


mysqli_close($mydb);


?>
