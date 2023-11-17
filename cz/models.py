# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Player(models.Model):
    playerid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    userid_pending = models.IntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    borncity = models.CharField(max_length=100)
    bornprovince = models.IntegerField()
    homecity = models.CharField(max_length=100)
    homeprovince = models.IntegerField()
    birthdate = models.DateField()
    hide_birthdate = models.IntegerField()
    dieddate = models.DateField()
    throws = models.IntegerField()
    startyear = models.IntegerField()
    height = models.DecimalField(max_digits=9, decimal_places=2)
    weight = models.IntegerField()
    family = models.TextField()
    employer = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=75)
    highschool = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    nationality = models.IntegerField()
    photo = models.IntegerField()
    photo_delivery = models.IntegerField()
    photo_sweeping = models.IntegerField()
    photo_house = models.IntegerField()
    photo_closeup = models.IntegerField()
    status = models.IntegerField()
    lastupdated = models.IntegerField()
    counter = models.IntegerField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    sub_register = models.IntegerField()
    sub_updates = models.IntegerField()
    twitter = models.CharField(max_length=50)
    widgetid = models.CharField(max_length=40)
    twitter_rating = models.IntegerField()
    facebook = models.CharField(max_length=150)
    wikipedia = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'player'
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Team(models.Model):
    teamid = models.IntegerField(primary_key=True)
    eventid = models.ForeignKey('Event', on_delete=models.DO_NOTHING, db_column='eventid')
    eventtypeid = models.IntegerField()
    drawid = models.IntegerField()
    status = models.IntegerField()
    fiveplayerteam = models.IntegerField()
    teamage = models.IntegerField()
    teamname_playerid = models.IntegerField()
    skip = models.ForeignKey('Player', related_name='teams_as_skip', on_delete=models.DO_NOTHING, db_column='skip')
    fourth = models.ForeignKey('Player', related_name='teams_as_fourth', on_delete=models.DO_NOTHING, db_column='fourth')
    third = models.ForeignKey('Player', related_name='teams_as_third', on_delete=models.DO_NOTHING, db_column='third')
    second = models.ForeignKey('Player', related_name='teams_as_second', on_delete=models.DO_NOTHING, db_column='second')
    lead = models.ForeignKey('Player', related_name='teams_as_lead', on_delete=models.DO_NOTHING, db_column='lead')
    spare = models.ForeignKey('Player', related_name='teams_as_spare', on_delete=models.DO_NOTHING, db_column='spare')
    coach = models.IntegerField()
    website = models.CharField(max_length=150)
    blogrss = models.CharField(max_length=150)
    twitter = models.CharField(max_length=100)
    twitter_rating = models.IntegerField()
    facebook = models.CharField(max_length=100)
    facebook_rating = models.IntegerField()
    facebookrss = models.CharField(max_length=150)
    youtube = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    sectionid = models.IntegerField()
    clubid = models.IntegerField()
    teamname = models.CharField(max_length=100)
    teamname_short = models.CharField(max_length=20)
    counter = models.IntegerField()
    dateline = models.IntegerField()
    submittedby = models.CharField(max_length=155)
    submittedemail = models.CharField(max_length=155)
    paid = models.IntegerField()
    paid_comments = models.TextField()
    sponsor = models.CharField(max_length=50)
    sponsorurl = models.CharField(max_length=150)
    photo = models.CharField(max_length=15)
    photodesc = models.CharField(max_length=255)
    tier = models.IntegerField()
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'team'

    def __str__(self):
        # Check if the skip is set, and return the skip's last name as the team name
        if self.skip:
            return self.skip.lastname
        else:
            # Provide a default string or the teamid if the skip is not set
            return f"Team {self.teamid}"
        
    @property
    def name(self):
        # Check if the skip is set, and return the skip's last name as the team name
        if self.skip:
            return f"Team {self.skip.lastname}"
        else:
            # Provide a default string or the teamid if the skip is not set
            return f"Team {self.teamid}"
        

class Event(models.Model):
    eventid = models.AutoField(primary_key=True)
    eventid_recovery = models.IntegerField()
    eventsetid = models.IntegerField()
    eventname = models.CharField(max_length=100)
    shortname = models.CharField(max_length=50)
    eventyear = models.IntegerField()
    startdate = models.DateField()
    enddate = models.DateField()
    city = models.CharField(max_length=50)
    sectionid = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    hosthotel = models.TextField()
    paymentinfo = models.TextField()
    purse = models.IntegerField()
    entryfee = models.IntegerField()
    localcurrency = models.IntegerField()
    conversion = models.DecimalField(max_digits=9, decimal_places=6)
    contact = models.CharField(max_length=50)
    contactphone = models.CharField(max_length=25)
    contactemail = models.CharField(max_length=100)
    contactfax = models.CharField(max_length=25)
    formattype = models.CharField(max_length=25)
    numteams = models.IntegerField()
    numqualify = models.IntegerField()
    qualifystructure = models.IntegerField()
    guaranteedgames = models.IntegerField()
    shootout = models.IntegerField()
    clubid = models.IntegerField()
    venueid = models.IntegerField()
    website = models.CharField(max_length=150)
    results = models.CharField(max_length=150)
    twitter = models.CharField(max_length=100)
    blogrss = models.CharField(max_length=255)
    facebook = models.CharField(max_length=50)
    facebookrss = models.CharField(max_length=50)
    entryform = models.CharField(max_length=150)
    entryformweb = models.CharField(max_length=150)
    logo = models.CharField(max_length=100)
    logo_lg = models.CharField(max_length=100)
    page_header_type = models.IntegerField()
    page_header_code = models.TextField()
    counter = models.IntegerField()
    eventscoring = models.IntegerField()
    timezoneid = models.IntegerField()
    scoreboard = models.IntegerField()
    scoreboard_short = models.CharField(max_length=15)
    eventid_pair = models.IntegerField()
    eventlabel = models.CharField(max_length=15)
    paypaladdress = models.CharField(max_length=155)
    paypalcode = models.TextField()
    onlineregister = models.IntegerField()
    onlineregisterlink = models.TextField()
    showteams = models.IntegerField()
    showteamsondraw = models.IntegerField()
    web = models.IntegerField()
    primarydraw = models.IntegerField()
    showteamname = models.IntegerField()
    strength_of_field = models.DecimalField(max_digits=7, decimal_places=4)
    strength_of_field2 = models.DecimalField(max_digits=7, decimal_places=4)
    reportpath = models.CharField(max_length=100)
    fantasynotification = models.IntegerField()
    lastscoresupdate = models.IntegerField()
    lastscoresfinal = models.IntegerField()
    weekfeatured = models.IntegerField()
    usetiers = models.IntegerField()
    hashtags = models.CharField(max_length=50)
    generatexml = models.IntegerField()
    donottweet = models.IntegerField()
    teams_update = models.IntegerField()
    stadiumid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event'


class Eventtournament(models.Model):
    eventid = models.IntegerField()
    tournamentid = models.IntegerField()
    tournamentlabel = models.CharField(max_length=50)
    classid = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventtournament'


class Clubs(models.Model):
    clubid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    facility_type = models.IntegerField()
    sheets = models.IntegerField()
    weeks = models.IntegerField()
    rental_rate_per_day = models.DecimalField(max_digits=9, decimal_places=2)
    leagues = models.IntegerField()
    address = models.CharField(max_length=100)
    mailaddress = models.CharField(max_length=100)
    city = models.CharField(max_length=75)
    province = models.IntegerField()
    country = models.IntegerField()
    postalcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=25)
    fax = models.CharField(max_length=25)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    blogrss = models.CharField(max_length=255)
    twitter = models.CharField(max_length=50)
    twitter_widget = models.TextField()
    twitter_rating = models.IntegerField()
    facebook = models.CharField(max_length=255)
    facebookrss = models.CharField(max_length=255)
    facebook_rating = models.IntegerField()
    googlemaps = models.CharField(max_length=255)
    logo = models.IntegerField()
    logosm = models.IntegerField()
    history = models.TextField()
    closed = models.IntegerField()
    origin = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clubs'


