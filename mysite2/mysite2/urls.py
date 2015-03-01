from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)), 
	
	url(r'^MyCourse/$','mycourse.views.MyCourse'),

	url(r'^update/$','lecture.views.lec_update'),
	url(r'^sel_period/(?P<period>\w+)/(?P<page>\d+)/$', 'schedule.views.SelectPeriod'),
)

urlpatterns += patterns('login.views',
	url(r'^Confirm/$','Confirm'),
	url(r'^HisnetCheck/$','HisnetCheck'),
	url(r'^Register/$','Register'),
	url(r'^$', 'loginCheck'),
	url(r'^Logout/$', 'logout_page'),
	
	)

urlpatterns += patterns('index.views',
	url(r'^Search/$', 'Search'),

	url(r'^MyPage/$', 'MyPage'), 
	url(r'^About/$','About'),
	url(r'^Schedule/$','Schedule'),
	url(r'^Judgement/$','Judgement'),
	url(r'^FirstMajorPage/(\d+)/$','Main'),
	url(r'^SecondMajorPage/(\d+)/$','Main'),
	url(r'^AllPage/(\d+)/$','Main'),
	url(r'^SubScript/$','SubScript'),
	url(r'^SiteMap/$','SiteMap'),
)

urlpatterns += patterns('recommend.views',
	url(r'^Recommend/(\d+)$','Recommend'),
	url(r'^Recommend/Recommend_Write$','Recommend_Write'),
	url(r'^Like/(\d+)$','Like'),

)

urlpatterns += patterns('qna.views',
	url(r'^QnA/page/(\d+)$','QnA'),
	url(r'^QnA/$','QnAMain'),
	url(r'^QnA/Write$','QnAWrite'),
	url(r'^QnA/Writing$','QnA_Writing'),
	url(r'^QnA/(\d+)/$','QnARead'),
	url(r'^QnA/Reply/(\d+)$','QnA_Reply'),
	url(r'^QnA/Replying/(\d+)$','QnA_Replying'),
)

urlpatterns += patterns('course.views',
	url(r'^Course/(\d+)$','Course'),
	url(r'^Course/(\d+)/Page/(\d+)$','CoursePage'),
)

urlpatterns += patterns('notice.views',
	url(r'^Notice/$','NoticeMain'),
	url(r'^Notice/Page/(\d+)$','Notice'),
	url(r'^Notice/(\d+)/$','Notice_Read'),
	url(r'^Notice/Write$', 'Notice_Write'),
	url(r'^Notice/Writing$', 'Notice_Writing'),
)