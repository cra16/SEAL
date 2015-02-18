from django.conf.urls import patterns, include, url

from login.views import *
from index.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^admin/', include(admin.site.urls)), 
	url(r'^$', loginCheck),
	url(r'^Logout/$', logout_page),
	url(r'^accouts/login/$', 'django.contrib.auth.views.login'),
#	url(r'^register/$', register),
#	url(r'^register/success/$', register_success),
	url(r'^MyPage/$', MyPage), 
    url(r'^About/$',About),
    url(r'^Schedule/$',Schedule),
    url(r'^Judgement/$',Judgement),
	url(r'^Recommend/(\d+)$','Recommend.views.Recommend'),
	url(r'^Recommend/Recommend_Write$','Recommend.views.Recommend_Write'),
	url(r'^QnA/page/(\d+)$','QnA.views.QnA'),
	url(r'^QnA/$','QnA.views.QnAMain'),
	url(r'^QnA/Write/$','QnA.views.QnAWrite'),
	url(r'^Course/(\d+)$','Course.views.Course'),
	url(r'^Course/(\d+)/Page/(\d+)$','Course.views.CoursePage'),
	url(r'^QnA/(\d+)/$','QnA.views.QnARead'),
	url(r'^Notice/$','Notice.views.NoticeMain'),
	url(r'^Notice/Page/(\d+)$','Notice.views.Notice'),
	url(r'^Notice/(\d+)/$','Notice.views.Notice_Read'),
	url(r'^FirstMajorPage/(\d+)/$',Main),
	url(r'^SecondMajorPage/(\d+)/$',Main),
	url(r'^AllPage/(\d+)/$',Main),
	url(r'^SubScript/$',SubScript),
	url(r'^SiteMap/$',SiteMap),
	url(r'^MyCourse/$',MyCourse),

#	url(r'^loginCheck/$', ),
#	url(r'^home/$', loginCheck)
	url(r'^update/$','lecture.views.lec_update'),
	url(r'^Confirm/$',Confirm),
	url(r'^HisnetCheck/$',HisnetCheck),
	url(r'^Register/$',Register),
	url(r'^sel_period/(\w+)$', 'schedule.views.SelectPeriod'),
)
