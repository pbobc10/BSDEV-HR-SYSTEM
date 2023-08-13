from django.core.management.base import BaseCommand
from ...calculate_easter_date import calculate_easter_date
from ...calculate_mardi_gras_date import calculate_mardi_gras_date
import datetime
from ...fiscal_year import FiscalYear
from ...models.days_off_models import DaysOff

class Command(BaseCommand):
    help = 'Command to add new Days off in the database.'
    

    def handle(self,*args,**options):
        fiscal_year = FiscalYear()
        current_year = datetime.date.today().year
        # mardi_gras
        annee, mois, jour = calculate_mardi_gras_date(current_year)
        mardi_gras = datetime.date(annee,mois,jour)
        mardi_gras_string = mardi_gras.strftime("%Y-%m-%d")
        # Easter
        easter_year, easter_month, easter_day = calculate_easter_date(current_year)
        easter = datetime.date(easter_year, easter_month, easter_day)
        easter_string = easter.strftime("%Y-%m-%d")
        days = [
                (f"{current_year-1}-11-18","commémoration de la bataille de Vertières et jour des forces armées d'Haïti"),
                (f"{current_year-1}-11-01"," fête de la Toussaint"),
                (f"{current_year-1}-11-02","jour de la fête des morts"),
                (f"{current_year-1}-12-05","anniversaire de la découverte d'Haïti"),
                (f"{current_year-1}-12-25","jour de Noël"), 
                (f"{current_year}-01-01"," jour de l'indépendance"),
                (f"{current_year}-01-02", "jour des aïeux"),
                (mardi_gras_string,"le Mardi gras"),
                (easter_string,"le Vendredi-Saint"),
                (f"{current_year}-05-01"," fête nationale du travail et de l'agriculture"),
                (f"{current_year}-05-18","fête du drapeau et de l'Université"),
                (f"{current_year}-05-22","jour de la souveraineté et de la reconnaissance nationale"),
                (f"{current_year}-06-22","jour de la présidence à vie"),
                ]
            
        
        if not DaysOff.objects.filter(fiscal_year=str(fiscal_year)).count():
            for day in days:
                DaysOff.objects.create(day=day[0],description=day[1],fiscal_year=str(fiscal_year))