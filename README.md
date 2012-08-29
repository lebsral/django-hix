django-hix
==========

Health Insurance Exchange.  Project for states to comply with the Afordable Care Act (ACA) insurance exchange setup.


glossary of terms
www.healthcare.gov/glossary/04262011a.pdf


Essential Health Benefits

    ambulatory patient services
    emergency services
    hospitalization
    maternity and newborn care
    mental health and substance use disorder services, including behavioral health treatment
    prescription drugs
    rehabilitative and habilitative services and devices
    laboratory services
    preventive and wellness services and chronic disease management
    and pediatric services, including oral and vision care





Setting Up:
1.  In the setting file
 change
 
 choose a database and change Default.  It is currently a sql lite 3.  Which is ok for
 testing but will not hold up to a production environment.

 
 TIME_ZONE = 'America/Chicago'
 to whatever your time zone is
 
 
 
  
 the default database superuser is:
 user: admin
 password:admin