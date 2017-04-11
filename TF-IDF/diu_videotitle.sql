-- 获取用户观看的视频标题列表,暂取1000个用户

hive -e "
select
u_diu,
collect_set(title)
from
(select u_diu, u_vid, f_hits from da.recy_als_data_uvr where dt='2017-04-10' ) a
join
(select vid, title, uid from dw.video where status=0 )  b
on(a.u_vid=b.vid)
group by
u_diu
limit 1000
">diu_videotitle.txt
