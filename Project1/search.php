<?php
require_once('dbinfo.php');

ini_set("display_errors","On");
error_reporting(E_ALL);
$search = isset($_POST['search'])?$_POST['search']:'';

$mydb = new mysqli($server_host,$user_name,$password,$db);

mysqli_connect_error()?die("数据库连接失败！"):'';




if($search==''){

  //  $sql_all = "select * from favorites";


// $sql_all="select favorites.id,favorites.name,favorites.comment,tag.tag_content
// from favorites_tag_relation
// left join favorites on favorites_tag_relation.id=favorites.id
// left join tag on favorites_tag_relation.tag_id=tag.tag_id";

$sql_all="select favorites.id,favorites.name,favorites.comment,tag.tag_content,tag.tag_id from favorites
    left join tag on favorites.tag_id=tag.tag_id";
     $results_array=array();
     $result=$mydb->query($sql_all);
      while($row=$result->fetch_row()){
        $results_array[]=$row;
        //echo $results_array;
      }

   echo json_encode($results_array);
}else{
    $sql_name = "select favorites.id,favorites.name,favorites.comment,tag.tag_content,tag.tag_id from favorites
    left join tag on favorites.tag_id=tag.tag_id where favorites.name = '$search' or tag.tag_content = '$search'" ;
// $sql_name="select favorites.id,favorites.name,favorites.comment,tag.tag_content,tag.tag_id
// from favorites_tag_relation
// left join favorites on favorites_tag_relation.id=favorites.id
// left join tag on favorites_tag_relation.tag_id=tag.tag_id
// where favorites.name='$search' or tag.tag_content='$search'
//
// ";
$results_arr=array();

$result = $mydb->query($sql_name);


 while($row=$result->fetch_row()){
   $results_arr[]=$row;
   //echo $results_array;
 }
// $sql="select tag.tag_content
// from tag
// left join favorites_tag_relation on favorites_tag_relation.tag_id=favorites.id
// left join  on favorites_tag_relation.tag_id=tag.tag_id
// where tag.tag_content='$s'"
// $result_a=$mydb->query($sql);
//
// $data=$result_a->fetch_all();
  echo json_encode($results_arr);
//  echo_json_ecode($data);

}


mysqli_close($mydb);
?>
