from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)), 
	url(r'^MyCourse/$','mycourse.views.MyCourse'),
	url(r'^MyCourseDelete/$','mycourse.views.CourseDelete'),
	url(r'^update/$','lecture.views.lec_update'),
	url(r'^DBUpdate/$','lecture.views.UpdateLogin'),
	url(r'^CurUpdate/$','lecture.views.AutoFastLecUpdate'),
	url(r'^MyCoursePage/$','mycourse.views.MyCoursePageNation'),
	
)

urlpatterns += patterns('schedule.views',
	url(r'^sel_period/(?P<period>\w+)/(?P<page>\d+)/$', 'SelectPeriod'),
	#url(r'^Schedule/Search/$','SearchSubject'),
	url(r'^Schedule/$','SearchSubject'),
	url(r'^Sel_lecture/$','SelectLecture'),
	url(r'^Sel_periodLecture/$','SearchSelectPeriod'),
	url(r'^Remove_lecture/$','RemoveLecture'),
	)#schedule view

urlpatterns += patterns('login.views',
	url(r'^Confirm/$','Confirm'),
	url(r'^HisnetCeck/$','HisnetCheck'),
	url(r'^Register/$','Register'),
	url(r'^RegisterInfo/$','RegisterInfo'),
	url(r'^$', 'loginCheck'),
	url(r'^Logout/$', 'logout_page'),
	)#login view

urlpatterns += patterns('index.views',
	url(r'^Search/$', 'Search'),
	url(r'^SearchPage/$','SearchPage'),
	url(r'^MyPage/$', 'MyPage'), 
	url(r'^About/$','About'),
	
	url(r'^Judgement/$','Judgement'),
	url(r'^Page/$','Page'),
	url(r'^SubScript/$','SubScript'),
	url(r'^SiteMap/$','SiteMap'),
	url(r'^FirstPage/$','Page'),
	url(r'^SecondPage/$','Page'),
	url(r'^ThirdPage/$','Page'),
	url(r'^Select_Course/$','Page'),
	url(r'^Select_Professor/$','Page')
)#mainPage view

urlpatterns += patterns('mypage.views',
	url(r'^MyPage/PasswordChange$', 'MyPagePassWordChange'),
)#mypage view

urlpatterns += patterns('recommend.views',
	url(r'^Recommend/(\d+)$','Recommend'),
	url(r'^Recommend/Recommend_Write$','Recommend_Write'),
	url(r'^Like/$','Like'),
	url(r'^NotEmptyRecommend/$','Recommend_NotEmpty')
)#recommend view

urlpatterns += patterns('qna.views',
	url(r'^QnA/Page/','QnA'),
	url(r'^QnA/$','QnAMain'),
	url(r'^QnA/Write$','QnAWrite'),
	url(r'^QnA/Writing$','QnA_Writing'),
	url(r'^QnA/(\d+)/$','QnARead'),
	url(r'^QnA/Reply/(\d+)$','QnA_Reply'),
	url(r'^QnA/Replying/(\d+)$','QnA_Replying'),

)

urlpatterns += patterns('course.views',
	url(r'^Course/(\d+)$','Course'),
	url(r'^CoursePageNation/(\d+)$','CoursePage'),
	url(r'^CourseProfessor/(\d+)$','CourseProfessor'),
	url(r'^Course/Period(\d+)$','PeriodCourse'),
	url(r'^CoursePageNation/(\w+)$','PeriodCoursePage')
) # course view

urlpatterns += patterns('notice.views',
	url(r'^Notice/$','NoticeMain'),
	url(r'^Notice/Page/','Notice'),
	url(r'^Notice/(\d+)/$','Notice_Read'),
	url(r'^Notice/Write$', 'Notice_Write'),
	url(r'^Notice/Writing$', 'Notice_Writing'),

)#Notice view