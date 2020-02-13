from django.conf import settings
from django.db import models
from django.utils import timezone

# Objektvorlage
# Klasse für zukünftige Objekte
# Post = Name des Models
# models.Model=gibt an, dass es ein Django Model ist, Django weiß, dass es in der Datenbank gespeichert werden soll
class Post(models.Model):
    # Felder und Typen definieren
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # definiert eine Verknüpfung/Beziehung zu einem anderen Model.
    title = models.CharField(max_length=200) # Textfeld mit limitierter Anzahl von Zeichen
    text = models.TextField() # So definierst du ein langes Textfeld ohne Grössenbeschränkung
    created_date = models.DateTimeField(default=timezone.now) # ein Feld für einen Zeitpunkt (ein Datum und eine Uhrzeit)
    published_date = models.DateTimeField(blank=True, null=True)

    # veröffentlich die Blogposts
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
