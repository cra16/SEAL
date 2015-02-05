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
	url(r'^Recommend/$',Recommend),
	url(r'^QnA/page/(\d+)$',QnA),
	url(r'^QnA/$',QnAMain),
	url(r'^QnA/Write/$',QnAWrite),
	url(r'^Course/$',Course),
	url(r'^QnA/(\d+)/$',QnARead),
	url(r'^Notice/$',NoticeMain),
	url(r'^Notice/Page/(\d+)$',Notice),
	url(r'^Notice/(\d+)/$',Notice_Read),
	url(r'^Confirm/$',Confirm),
	url(r'^Register/$',Register),
	url(r'^(\d+)/$',Main),
#	url(r'^loginCheck/$', ),
#	url(r'^home/$', loginCheck)
	url(r'^update/$','lecture.views.lec_update'),

)
