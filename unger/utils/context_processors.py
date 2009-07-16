from django.core.urlresolvers import reverse

def user(request):
  return {
  	"user":request.user,
	}

class Link(object):
  def __init__(self, name, href):
    self.name = name
    self.href = href

def nav_links(request):
  links = (
    Link("Expenses",reverse("expenses")),
    Link("Spending Targets",reverse("spending_target")),
    Link("Profile",reverse("profile")),
  )
  return {'nav_links':links}

LOADED_PROCESSORS = (
  user,
  nav_links,
)

def processor(request):
  out_dict = {}
  for p in LOADED_PROCESSORS:
    out_dict.update(p(request))
  return out_dict
