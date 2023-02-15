from django.contrib import admin
from .models import User, Skill, SocialMedia

# Register Models
admin.site.register(User)
admin.site.register(Skill)
admin.site.register(SocialMedia)