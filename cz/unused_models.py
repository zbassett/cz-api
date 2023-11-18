








class Access(models.Model):
    userid = models.PositiveIntegerField()
    forumid = models.PositiveSmallIntegerField()
    accessmask = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'access'


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class Adminlog(models.Model):
    adminlogid = models.AutoField(primary_key=True)
    userid = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()
    script = models.CharField(max_length=20)
    action = models.CharField(max_length=20)
    extrainfo = models.CharField(max_length=200)
    ipaddress = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'adminlog'


class Adminutil(models.Model):
    title = models.CharField(max_length=10)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'adminutil'


class AnalyticsAccount(models.Model):
    accountid = models.AutoField(primary_key=True)
    accountname = models.CharField(max_length=100)
    baseurl = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analytics_account'


class AnalyticsAccountSocial(models.Model):
    asid = models.AutoField(primary_key=True)
    accountid = models.IntegerField()
    platformid = models.IntegerField()
    socialname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'analytics_account_social'


class AnalyticsFile(models.Model):
    fileid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    filename = models.TextField()
    filesize = models.IntegerField()
    filetype = models.TextField()
    filedate = models.IntegerField()
    filedesc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analytics_file'


class AnalyticsSocial(models.Model):
    socialid = models.AutoField(primary_key=True)
    aeid = models.IntegerField()
    platformid = models.IntegerField()
    accountid = models.IntegerField()
    mention = models.CharField(max_length=100)
    postcount = models.IntegerField()
    impressions = models.IntegerField()
    eventid = models.IntegerField()
    stadiumid = models.IntegerField()
    lastupdate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analytics_social'


class AnalyticsSocialPlatform(models.Model):
    platformid = models.AutoField(primary_key=True)
    platform = models.CharField(max_length=100)
    baseurl = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analytics_social_platform'


class AnalyticsTeamPermission(models.Model):
    permid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analytics_team_permission'


class AnalyticsTeamReport(models.Model):
    reportid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    datetime = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analytics_team_report'


class AnalyticsWebsite(models.Model):
    aid = models.AutoField(primary_key=True)
    eventweekid = models.IntegerField()
    eventid = models.IntegerField()
    gameid = models.IntegerField()
    teamid = models.IntegerField()
    postid = models.IntegerField()
    data_users = models.IntegerField()
    data_new_users = models.IntegerField()
    data_sessions = models.IntegerField()
    data_sessions_per_user = models.DecimalField(max_digits=9, decimal_places=2)
    data_pageviews = models.IntegerField()
    data_pageviews_unique = models.IntegerField()
    data_avg_time_on_page = models.IntegerField()
    data_pages_per_session = models.DecimalField(max_digits=9, decimal_places=2)
    data_avg_session_duration = models.IntegerField()
    data_bounce_rate = models.DecimalField(max_digits=9, decimal_places=2)
    lastupdate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analytics_website'


class Announcement(models.Model):
    announcementid = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    userid = models.PositiveIntegerField()
    startdate = models.PositiveIntegerField()
    enddate = models.PositiveIntegerField()
    pagetext = models.TextField()
    forumid = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'announcement'


class Attachment(models.Model):
    attachmentid = models.SmallAutoField(primary_key=True)
    userid = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()
    filename = models.CharField(max_length=100)
    filedata = models.TextField()
    visible = models.PositiveSmallIntegerField()
    private = models.PositiveIntegerField()
    counter = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'attachment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Avatar(models.Model):
    avatarid = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    minimumposts = models.SmallIntegerField()
    avatarpath = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'avatar'


class Bbcode(models.Model):
    bbcodeid = models.SmallAutoField(primary_key=True)
    bbcodetag = models.CharField(max_length=200)
    bbcodereplacement = models.CharField(max_length=200)
    bbcodeexample = models.CharField(max_length=200)
    bbcodeexplanation = models.TextField()
    twoparams = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'bbcode'


class Blog(models.Model):
    blogid = models.AutoField(primary_key=True)
    blogname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    userid = models.IntegerField()
    image_lg = models.CharField(max_length=50)
    image_sm = models.CharField(max_length=50)
    feedurl = models.CharField(max_length=255)
    feedname = models.CharField(max_length=20)
    podcast = models.IntegerField()
    featured = models.IntegerField()
    active = models.IntegerField()
    autogen = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blog'


class BlogContent(models.Model):
    blogid = models.IntegerField(primary_key=True)
    blogtitle = models.CharField(max_length=100)
    blogurl = models.CharField(max_length=150)
    blogdesc = models.CharField(max_length=250, db_collation='utf8_unicode_ci')
    blogcontent = models.TextField()
    podcastembed = models.TextField()
    blogdate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blog_content'


class Bracketgame(models.Model):
    bracketgameid = models.AutoField(primary_key=True)
    drawid = models.IntegerField()
    locationid = models.IntegerField()
    gamedatetime = models.CharField(max_length=30)
    gametime = models.IntegerField()
    tournamentid = models.IntegerField()
    no_connection_tournamentid = models.IntegerField()
    teamid1 = models.IntegerField()
    teamid2 = models.IntegerField()
    teamid1_ranking = models.IntegerField()
    teamid2_ranking = models.IntegerField()
    teamid_top = models.IntegerField()
    teamid_bottom = models.IntegerField()
    format = models.IntegerField()
    tournamentgameid = models.IntegerField()
    gamelabel = models.CharField(max_length=50)
    loserlabel = models.CharField(max_length=50)
    gameid = models.IntegerField(blank=True, null=True)
    tier = models.IntegerField()
    lastupdated = models.IntegerField()
    dataconvert = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bracketgame'


class Bracketlocation(models.Model):
    format = models.IntegerField(primary_key=True)
    tournamentgameid = models.IntegerField()
    winnergame = models.IntegerField()
    winnergamelocation = models.IntegerField()
    losergame = models.IntegerField()
    losergamelocation = models.IntegerField()
    winner2game = models.IntegerField()
    winner2gamelocation = models.IntegerField()
    gamename = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'bracketlocation'
        unique_together = (('format', 'tournamentgameid'),)


class BracketlocationLabel(models.Model):
    labelid = models.AutoField(primary_key=True)
    tournamentid = models.IntegerField()
    format = models.IntegerField()
    tournamentgameid = models.IntegerField()
    labeltext = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bracketlocation_label'


class BracketlocationOverride(models.Model):
    overrideid = models.AutoField(primary_key=True)
    tournamentid = models.IntegerField()
    tournamentgameid = models.IntegerField()
    winnergame = models.IntegerField()
    winnergamelocation = models.IntegerField()
    losergame = models.IntegerField()
    losergamelocation = models.IntegerField()
    winner2game = models.IntegerField()
    winner2gamelocation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bracketlocation_override'


class Bracketlocationgame(models.Model):
    bracketgameid = models.IntegerField()
    tournamentgameid = models.IntegerField()
    format = models.IntegerField()
    tournamentid = models.IntegerField()
    gamelabel = models.CharField(max_length=100)
    loserlabel = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'bracketlocationgame'


class CalendarEvents(models.Model):
    eventid = models.AutoField(primary_key=True)
    userid = models.PositiveIntegerField()
    event = models.TextField()
    eventdate = models.DateField()
    public = models.PositiveSmallIntegerField()
    subject = models.CharField(max_length=254)
    allowsmilies = models.SmallIntegerField()
    clubid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'calendar_events'


class Cartoon(models.Model):
    cartoonid = models.AutoField(primary_key=True)
    authorid = models.IntegerField()
    cartoonfile = models.CharField(max_length=50)
    cartoontitle = models.CharField(max_length=255)
    cartoondesc = models.TextField()
    cartoondate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cartoon'


class CartoonAuthor(models.Model):
    authorid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cartoon_author'


class CcrYears(models.Model):
    year = models.IntegerField()
    year_name = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'ccr_years'


class ClubBonspielType(models.Model):
    typeid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=25)
    tier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'club_bonspiel_type'


class ClubLeagueType(models.Model):
    typeid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=25)
    tier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'club_league_type'


class ClubPracticeType(models.Model):
    typeid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=25)
    tier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'club_practice_type'


class Clubphoto(models.Model):
    photoid = models.AutoField(primary_key=True)
    photosetid = models.IntegerField()
    image = models.CharField(max_length=50)
    headline = models.CharField(max_length=100)
    caption = models.CharField(max_length=255)
    photodate = models.DateField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clubphoto'


class Clubphotoset(models.Model):
    photosetid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    photosetdate = models.DateField()
    photosetname = models.CharField(max_length=100)
    photosetcaption = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'clubphotoset'





class ClubsAdmin(models.Model):
    adminid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    userid = models.IntegerField()
    display_name = models.IntegerField()
    adminlevel = models.IntegerField()
    manager = models.IntegerField()
    status = models.IntegerField()
    dateregistered = models.IntegerField()
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'clubs_admin'


class ClubsAdminPermission(models.Model):
    permid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'clubs_admin_permission'


class ClubsAssetPrice(models.Model):
    cpid = models.AutoField(primary_key=True)
    assetid = models.IntegerField()
    clubid = models.IntegerField()
    level = models.IntegerField()
    value = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'clubs_asset_price'


class ClubsBonspiel(models.Model):
    leagueid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    typeid = models.IntegerField()
    count = models.IntegerField()
    ends = models.IntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'clubs_bonspiel'


class ClubsLeague(models.Model):
    leagueid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    typeid = models.IntegerField()
    count = models.IntegerField()
    ends = models.IntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'clubs_league'


class ClubsLevelValue(models.Model):
    valueid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    level = models.IntegerField()
    value = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'clubs_level_value'


class ClubsPhoto(models.Model):
    photoid = models.IntegerField()
    clubid = models.IntegerField()
    userid = models.IntegerField()
    user_submitted = models.IntegerField()
    mainphoto = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clubs_photo'


class ClubsPractice(models.Model):
    leagueid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    typeid = models.IntegerField()
    count = models.IntegerField()
    minutes = models.IntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'clubs_practice'


class ClubsSheet(models.Model):
    clubid = models.IntegerField()
    sheetname = models.CharField(max_length=25)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clubs_sheet'


class Commentary(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.IntegerField()
    category = models.IntegerField()
    commentarydate = models.DateField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'commentary'


class Commentaryauthor(models.Model):
    authorid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    authortitle = models.CharField(max_length=100)
    columntitle = models.CharField(max_length=50)
    headlinename = models.CharField(max_length=75)
    imagename = models.CharField(max_length=75)
    authorbio = models.TextField()

    class Meta:
        managed = False
        db_table = 'commentaryauthor'


class Competitor(models.Model):
    competitorid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    pprovince = models.IntegerField()
    teamid = models.IntegerField()
    tourteamid = models.IntegerField()
    drawid = models.IntegerField()
    winner = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'competitor'


class Customavatar(models.Model):
    userid = models.PositiveIntegerField(primary_key=True)
    avatardata = models.TextField()
    dateline = models.PositiveIntegerField()
    filename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'customavatar'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'





class EventAssetPrice(models.Model):
    cpid = models.AutoField(primary_key=True)
    assetid = models.IntegerField()
    clubid = models.IntegerField()
    eventid = models.IntegerField()
    level = models.IntegerField()
    value = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'event_asset_price'


class EventBlog(models.Model):
    eventblogid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    blogrss = models.CharField(max_length=150)
    userid = models.IntegerField()
    dateupdated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_blog'


class EventBudgetItem(models.Model):
    itemid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    item_name = models.CharField(max_length=25)
    item_value = models.DecimalField(max_digits=9, decimal_places=2)
    item_desc = models.TextField()
    item_type = models.IntegerField()
    split_eventid = models.IntegerField()
    split_itemid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_budget_item'


class EventChecklist(models.Model):
    eventid = models.IntegerField()
    itemid = models.IntegerField()
    status = models.IntegerField()
    checkdate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_checklist'


class EventEmailLog(models.Model):
    emailid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    userid = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sendheaders = models.TextField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_email_log'


class EventEmailPlayer(models.Model):
    logid = models.AutoField(primary_key=True)
    emailid = models.IntegerField()
    teamid = models.IntegerField()
    playerid = models.IntegerField()
    email = models.CharField(max_length=100)
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_email_player'


class EventHistory(models.Model):
    historyid = models.AutoField(primary_key=True)
    eventsetid = models.IntegerField()
    history_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_history'


class EventInviteSent(models.Model):
    inviteid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    teamid = models.IntegerField()
    datesent = models.IntegerField()
    emailid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_invite_sent'


class EventMedia(models.Model):
    mediaid = models.AutoField(primary_key=True)
    eventsetid = models.IntegerField()
    media_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_media'


class EventNews(models.Model):
    linkid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    postid = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_news'


class EventPromoteLink(models.Model):
    linkid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    linkname = models.CharField(max_length=255)
    linkurl = models.CharField(max_length=255)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_promote_link'


class EventPromoteSent(models.Model):
    promoteid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()
    regionid = models.IntegerField()
    userid = models.IntegerField()
    tweet = models.CharField(max_length=150)
    message = models.CharField(max_length=150)
    hashtags = models.CharField(max_length=50)
    linkid = models.IntegerField()
    urlshort = models.CharField(max_length=50)
    datesent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_promote_sent'


class EventRules(models.Model):
    rulesid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    rules_desc = models.TextField()

    class Meta:
        managed = False
        db_table = 'event_rules'


class EventShootout(models.Model):
    shootoutid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    type = models.IntegerField()
    measure = models.IntegerField()
    ordersort = models.IntegerField()
    shotcount = models.IntegerField()
    shotdrop = models.IntegerField()
    shotdisplay = models.IntegerField()
    locked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_shootout'


class EventShootoutGame(models.Model):
    esgid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    tournamentid = models.IntegerField()
    tournamentteamid = models.IntegerField()
    gameid = models.IntegerField()
    shootout = models.DecimalField(max_digits=8, decimal_places=2)
    measure = models.IntegerField()
    include = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_shootout_game'


class EventShootoutTeam(models.Model):
    shootteamid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    teamid = models.IntegerField()
    fourth = models.DecimalField(max_digits=8, decimal_places=3)
    third = models.DecimalField(max_digits=8, decimal_places=3)
    second = models.DecimalField(max_digits=8, decimal_places=3)
    lead = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'event_shootout_team'


class EventSponsor(models.Model):
    sponsorid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    sponsor_level_id = models.IntegerField()
    sponsorname = models.CharField(max_length=100)
    sponsordescription = models.TextField()
    sponsorurl = models.CharField(max_length=255)
    sponsorimage = models.CharField(max_length=255)
    sponsorthumb = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'event_sponsor'


class EventSponsorLevel(models.Model):
    sponsor_level_id = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    sponsor_level = models.CharField(max_length=50)
    level_value = models.TextField()
    priority = models.IntegerField()
    eventfront = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_sponsor_level'


class EventTeamInvoice(models.Model):
    eventid = models.IntegerField()
    teamid = models.IntegerField()
    base = models.DecimalField(max_digits=9, decimal_places=2)
    tax1 = models.DecimalField(max_digits=9, decimal_places=2)
    tax1_desc = models.CharField(max_length=50)
    tax2 = models.DecimalField(max_digits=9, decimal_places=2)
    tax2_desc = models.CharField(max_length=50)
    fees1 = models.DecimalField(max_digits=9, decimal_places=2)
    fees1_desc = models.CharField(max_length=50)
    fees2 = models.DecimalField(max_digits=9, decimal_places=2)
    fees2_desc = models.CharField(max_length=50)
    lastsentdate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_team_invoice'


class EventTeamLog(models.Model):
    logid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    teamid = models.IntegerField()
    userid = models.IntegerField()
    logdate = models.IntegerField()
    emailid = models.IntegerField()
    logdetail = models.TextField()
    sendto = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'event_team_log'


class EventTicket(models.Model):
    ticketid = models.IntegerField()
    eventid = models.IntegerField()
    ticket_headline = models.CharField(max_length=150)
    ticket_front = models.TextField()
    ticket_main = models.TextField()
    ticket_url = models.CharField(max_length=250)
    ticket_img = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'event_ticket'


class EventUserApplication(models.Model):
    eventuserid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    userid = models.IntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    notes = models.TextField()
    dateregistered = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_user_application'


class EventVenue(models.Model):
    venueid = models.AutoField(primary_key=True)
    venue_name = models.CharField(max_length=100)
    venue_desc = models.TextField()
    venue_address = models.CharField(max_length=100)
    venue_city = models.CharField(max_length=100)
    venue_province = models.IntegerField()
    venue_country = models.IntegerField()
    venue_postal = models.CharField(max_length=20)
    venue_url = models.CharField(max_length=250)
    venue_photoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_venue'


class EventVenueLink(models.Model):
    eventid = models.IntegerField()
    venueid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_venue_link'


class EventWatchcode(models.Model):
    watchid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    videotypeid = models.IntegerField()
    watchcode = models.TextField()
    watchlink = models.TextField()
    streamcode = models.TextField()
    streamlink = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'event_watchcode'


class Eventallstar(models.Model):
    eventid = models.IntegerField(primary_key=True)
    position = models.IntegerField()
    team = models.IntegerField()
    playerid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventallstar'
        unique_together = (('eventid', 'position', 'team'),)


class Eventclub(models.Model):
    eventid = models.IntegerField()
    clubid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventclub'


class Eventfile(models.Model):
    fileid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    filename = models.CharField(max_length=100)
    filedesc = models.CharField(max_length=255)
    filesize = models.IntegerField()
    filetype = models.CharField(max_length=5)
    filedate = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventfile'


class Eventlevel(models.Model):
    level = models.IntegerField(primary_key=True)
    levelname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'eventlevel'


class Eventlink(models.Model):
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()
    typetier = models.IntegerField()
    special = models.IntegerField()
    level = models.IntegerField()
    regionid = models.IntegerField()
    rr_tournamentid = models.IntegerField()
    tb_tournamentid = models.IntegerField()
    po_tournamentid = models.IntegerField()
    featuredweek = models.IntegerField()
    fantasy = models.IntegerField()
    invoice = models.IntegerField()
    dataconvert = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventlink'


class Eventpair(models.Model):
    eventid_primary = models.IntegerField()
    eventid_secondary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventpair'


class Eventphoto(models.Model):
    epid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    flickrid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'eventphoto'


class Eventplayerlist(models.Model):
    eventtypeid = models.IntegerField()
    oomtypeid = models.IntegerField()
    playerid = models.IntegerField()
    position = models.IntegerField()
    label = models.CharField(max_length=10)
    eventyear = models.IntegerField()
    moneytotal = models.IntegerField()
    pointtotal = models.DecimalField(max_digits=8, decimal_places=3)
    pointtotal_two = models.DecimalField(max_digits=8, decimal_places=3)
    currentrank = models.IntegerField()
    lastrank = models.IntegerField()
    lastmoneytotal = models.IntegerField()
    lastpointtotal = models.DecimalField(max_digits=8, decimal_places=3)
    lastpointtotal_two = models.DecimalField(max_digits=8, decimal_places=3)
    lastdate = models.DateField()
    ctrs_registered = models.IntegerField()
    statsrun = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventplayerlist'


class Eventrecord(models.Model):
    teamid = models.IntegerField()
    eventid = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    winner = models.IntegerField()
    shootout = models.DecimalField(max_digits=9, decimal_places=2)
    orderlock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventrecord'


class Eventset(models.Model):
    eventsetid = models.IntegerField()
    eventsetdesc = models.CharField(max_length=50)
    gender = models.IntegerField()
    eventset_pair = models.IntegerField()
    logo100 = models.CharField(max_length=100)
    logo250 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'eventset'


class Eventteamlist(models.Model):
    eventtypeid = models.IntegerField()
    teamid = models.IntegerField()
    oomtypeid = models.IntegerField()
    fiveplayerteam = models.IntegerField()
    skip = models.IntegerField()
    label = models.CharField(max_length=10)
    eventyear = models.IntegerField()
    moneytotal = models.IntegerField()
    pointtotal = models.DecimalField(max_digits=8, decimal_places=3)
    pointtotal_two = models.DecimalField(max_digits=8, decimal_places=3)
    currentrank = models.IntegerField()
    lastrank = models.IntegerField()
    lastmoneytotal = models.IntegerField()
    lastpointtotal = models.DecimalField(max_digits=8, decimal_places=3)
    lastpointtotal_two = models.DecimalField(max_digits=8, decimal_places=3)
    lastdate = models.DateField()
    ctrs_registered = models.IntegerField()
    teamage = models.IntegerField()
    statsrun = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventteamlist'


class Eventteamtourlink(models.Model):
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()
    teamid_event = models.IntegerField()
    teamid_tour = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventteamtourlink'


class Eventtournament(models.Model):
    eventid = models.IntegerField()
    tournamentid = models.IntegerField()
    tournamentlabel = models.CharField(max_length=50)
    classid = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventtournament'


class EventtournamentClass(models.Model):
    classid = models.AutoField(primary_key=True)
    tournamentclass = models.CharField(max_length=25)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventtournament_class'


class Eventtype(models.Model):
    eventtypeid = models.IntegerField(primary_key=True)
    eventtype = models.CharField(max_length=50)
    tourlinkid = models.IntegerField()
    division = models.CharField(max_length=50)
    is_doubles = models.IntegerField()
    shortform = models.CharField(max_length=10)
    directory = models.CharField(max_length=50)
    forumid = models.IntegerField()
    imagelogo = models.CharField(max_length=100)
    regionid = models.IntegerField()
    level = models.IntegerField()
    url = models.CharField(max_length=255)
    facebook = models.CharField(max_length=100)
    facebookid = models.IntegerField()
    twitter = models.CharField(max_length=25)
    hashtag = models.CharField(max_length=15)
    register = models.IntegerField()
    featured = models.IntegerField()
    category = models.IntegerField()
    color1 = models.CharField(max_length=10)
    color2 = models.CharField(max_length=10)
    teams_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventtype'


class EventtypeContact(models.Model):
    contactid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact_title = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=25)
    contact_email = models.CharField(max_length=100)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventtype_contact'


class EventtypeStrengthOfSchedule(models.Model):
    sosid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    teamid = models.IntegerField()
    totalgames = models.IntegerField()
    calcsos = models.DecimalField(db_column='calcSoS', max_digits=9, decimal_places=2)  # Field name made lowercase.
    countoomranking10 = models.IntegerField(db_column='countOOMranking10')  # Field name made lowercase.
    countoomranking10_win = models.IntegerField(db_column='countOOMranking10_win')  # Field name made lowercase.
    countoomranking10_loss = models.IntegerField(db_column='countOOMranking10_loss')  # Field name made lowercase.
    countoomranking10_tie = models.IntegerField(db_column='countOOMranking10_tie')  # Field name made lowercase.
    countoomranking25 = models.IntegerField(db_column='countOOMranking25')  # Field name made lowercase.
    countoomranking25_win = models.IntegerField(db_column='countOOMranking25_win')  # Field name made lowercase.
    countoomranking25_loss = models.IntegerField(db_column='countOOMranking25_loss')  # Field name made lowercase.
    countoomranking25_tie = models.IntegerField(db_column='countOOMranking25_tie')  # Field name made lowercase.
    countoomranking50 = models.IntegerField(db_column='countOOMranking50')  # Field name made lowercase.
    countoomranking50_win = models.IntegerField(db_column='countOOMranking50_win')  # Field name made lowercase.
    countoomranking50_loss = models.IntegerField(db_column='countOOMranking50_loss')  # Field name made lowercase.
    countoomranking50_tie = models.IntegerField(db_column='countOOMranking50_tie')  # Field name made lowercase.
    countoomranking100 = models.IntegerField(db_column='countOOMranking100')  # Field name made lowercase.
    countoomranking100_win = models.IntegerField(db_column='countOOMranking100_win')  # Field name made lowercase.
    countoomranking100_loss = models.IntegerField(db_column='countOOMranking100_loss')  # Field name made lowercase.
    countoomranking100_tie = models.IntegerField(db_column='countOOMranking100_tie')  # Field name made lowercase.
    countoomranking150 = models.IntegerField(db_column='countOOMranking150')  # Field name made lowercase.
    countoomranking150_win = models.IntegerField(db_column='countOOMranking150_win')  # Field name made lowercase.
    countoomranking150_loss = models.IntegerField(db_column='countOOMranking150_loss')  # Field name made lowercase.
    countoomranking150_tie = models.IntegerField(db_column='countOOMranking150_tie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventtype_strength_of_schedule'


class EventtypeUser(models.Model):
    etuserid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    userid = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventtype_user'


class Eventtypeyear(models.Model):
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    sponsor = models.CharField(max_length=100)
    moneylisttype = models.IntegerField()
    standingtype = models.IntegerField()
    qualifyonly = models.IntegerField()
    minimumgames_override = models.IntegerField()
    invoice_team_value = models.DecimalField(max_digits=9, decimal_places=2)
    invoice_event_value = models.DecimalField(max_digits=9, decimal_places=2)
    invoice_tier_value = models.DecimalField(max_digits=9, decimal_places=2)
    teams_update = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventtypeyear'


class EventtypeyearInvoice(models.Model):
    invoiceid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    eventyear = models.IntegerField()
    eventtypeid = models.IntegerField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    paid = models.DecimalField(max_digits=9, decimal_places=2)
    paiddate = models.IntegerField()
    sentdate = models.IntegerField()
    notes = models.TextField()
    sponsored = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventtypeyear_invoice'


class Eventweb(models.Model):
    eventid = models.IntegerField()
    skinid = models.IntegerField()
    branchid = models.IntegerField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'eventweb'


class EventwebSkin(models.Model):
    skinid = models.IntegerField()
    eventskin_name = models.CharField(max_length=50)
    eventtypeid = models.IntegerField()
    regionid = models.IntegerField()
    level = models.IntegerField()
    twitter = models.CharField(max_length=50)
    hashtag = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'eventweb_skin'


class EventwebSkinUser(models.Model):
    skinuserid = models.AutoField(primary_key=True)
    skinid = models.IntegerField()
    userid = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventweb_skin_user'


class EventwebSubhead(models.Model):
    skinid = models.IntegerField()
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()
    regionid = models.IntegerField()
    title = models.IntegerField()
    location = models.IntegerField()
    eventdate = models.IntegerField()
    menu = models.IntegerField()
    menu_pair = models.IntegerField()
    eventlogo = models.IntegerField()
    section_title = models.IntegerField()
    extendedrr = models.IntegerField()
    content_width = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventweb_subhead'


class Eventweek(models.Model):
    eventweek = models.IntegerField()
    eventyear = models.IntegerField()
    weekcount = models.IntegerField()
    tuesday = models.IntegerField()
    monday = models.IntegerField()
    featured = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventweek'


class EventweekEvent(models.Model):
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()
    regionid = models.IntegerField()
    eventyear = models.IntegerField()
    eventweek_start = models.IntegerField()
    eventweek_end = models.IntegerField()
    tourweek = models.IntegerField()
    calc_standings = models.IntegerField()
    calc_statistics = models.IntegerField()
    eventweek_lock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventweek_event'


class Eventweekfeatured(models.Model):
    eventtypeid = models.IntegerField()
    regionid = models.IntegerField()
    tourweek = models.IntegerField()
    eventweek = models.IntegerField()
    eventyear = models.IntegerField()
    featured = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventweekfeatured'


class FantasyCapGroup(models.Model):
    capid = models.IntegerField()
    userid = models.IntegerField()
    grouptag = models.CharField(max_length=30)
    grouptext = models.TextField()
    passcode = models.CharField(max_length=100)
    public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_cap_group'


class FantasyCapSettings(models.Model):
    capid = models.AutoField(primary_key=True)
    gamename = models.CharField(max_length=150)
    budget = models.IntegerField()
    eventid_one = models.IntegerField()
    eventone_count = models.IntegerField()
    eventid_two = models.IntegerField()
    eventtwo_count = models.IntegerField()
    marketing = models.TextField()
    rules = models.TextField()
    logourl = models.CharField(max_length=100)
    register_open = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_cap_settings'


class FantasyCapStatDefault(models.Model):
    statname = models.CharField(max_length=50)
    stattype = models.IntegerField()
    statvalue = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_cap_stat_default'


class FantasyCapTeam(models.Model):
    capid = models.IntegerField()
    teamid = models.IntegerField()
    eventid = models.IntegerField()
    value = models.IntegerField()
    points = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'fantasy_cap_team'


class FantasyCapTeamStat(models.Model):
    capid = models.IntegerField()
    statid = models.IntegerField()
    teamid = models.IntegerField()
    statcount = models.IntegerField()
    statvalue = models.DecimalField(max_digits=8, decimal_places=3)
    stattotal = models.DecimalField(max_digits=8, decimal_places=3)
    lastupdated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_cap_team_stat'


class FantasyCapUser(models.Model):
    fid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    capid = models.IntegerField()
    teamid = models.IntegerField()
    teamname = models.CharField(max_length=50)
    createdate = models.IntegerField()
    lastupdate = models.IntegerField()
    points = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'fantasy_cap_user'


class FantasyCapUserTeam(models.Model):
    fid = models.IntegerField()
    userid = models.IntegerField()
    capid = models.IntegerField()
    teamid = models.IntegerField()
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    value = models.IntegerField()
    adddate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_cap_user_team'


class FantasyEventStandings(models.Model):
    stid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    userid = models.IntegerField()
    teamid = models.IntegerField()
    win = models.IntegerField()
    loss = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_event_standings'


class FantasyGroup(models.Model):
    groupid = models.AutoField(primary_key=True)
    eventyear = models.IntegerField()
    eventtypeid = models.IntegerField()
    creator = models.IntegerField()
    groupname = models.CharField(max_length=30)
    teams = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_group'


class FantasyPick(models.Model):
    pickid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    teamname = models.CharField(max_length=25)
    points = models.IntegerField()
    rank = models.IntegerField()
    lastpoints = models.IntegerField()
    lastrank = models.IntegerField()
    lastupdated = models.IntegerField()
    dateregistered = models.IntegerField()
    emailnotify = models.IntegerField()
    emailnotifyaddress = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'fantasy_pick'


class FantasyPickEvent(models.Model):
    pickeventid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    eventid = models.IntegerField()
    userid = models.IntegerField()
    points = models.IntegerField()
    maxpoints = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_pick_event'


class FantasyPickGame(models.Model):
    pickgameid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    gameid = models.IntegerField()
    userid = models.IntegerField()
    teamid1 = models.IntegerField()
    teamid2 = models.IntegerField()
    dateset = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_pick_game'


class FantasyPickGroup(models.Model):
    pickgroupid = models.AutoField(primary_key=True)
    groupid = models.IntegerField()
    userid = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_pick_group'


class FantasyPickem(models.Model):
    pickemid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    userid = models.IntegerField()
    eventyear = models.IntegerField()
    totalpicks = models.IntegerField()
    correct = models.IntegerField()
    waiting = models.IntegerField()
    subscribe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_pickem'


class FantasyPickemContest(models.Model):
    contestid = models.IntegerField()
    contest_title = models.CharField(max_length=255)
    contest_teaser = models.TextField()
    contest_promo = models.TextField()
    contest_rules = models.TextField()
    contest_image_220x90 = models.CharField(max_length=255)
    contest_image_680x80 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'fantasy_pickem_contest'


class FantasyPickemContestEvent(models.Model):
    contest_eventid = models.AutoField(primary_key=True)
    contestid = models.IntegerField()
    eventid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_pickem_contest_event'


class FantasyPickemGame(models.Model):
    pickemgameid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    gameid = models.IntegerField()
    eventid = models.IntegerField()
    winnerteamid = models.IntegerField()
    loserteamid = models.IntegerField()
    pickdate = models.IntegerField()
    ipaddress = models.CharField(max_length=20)
    correct = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_pickem_game'


class FantasyPickemTitle(models.Model):
    titleid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    userid = models.IntegerField()
    titletypeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasy_pickem_title'


class Fantasyleague(models.Model):
    leagueid = models.IntegerField(primary_key=True)
    poolid = models.IntegerField()
    leaguename = models.CharField(max_length=100)
    teamcount = models.IntegerField()
    publicleague = models.IntegerField()
    password = models.CharField(max_length=50)
    commish = models.IntegerField()
    commishnotes = models.TextField()

    class Meta:
        managed = False
        db_table = 'fantasyleague'


class Fantasyleagueteam(models.Model):
    leagueid = models.IntegerField()
    teamid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasyleagueteam'


class Fantasymessage(models.Model):
    messageid = models.IntegerField()
    leagueid = models.IntegerField()
    teamid = models.IntegerField()
    messagetitle = models.CharField(max_length=150)
    messagetext = models.TextField()
    date = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'fantasymessage'


class Fantasypicks(models.Model):
    teamid = models.IntegerField()
    cteamid = models.IntegerField()
    rank = models.IntegerField()
    eventid = models.IntegerField()
    complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasypicks'


class Fantasypickstie(models.Model):
    teamid = models.IntegerField()
    winningteam = models.IntegerField()
    totalpoints = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fantasypickstie'


class Fantasypoints(models.Model):
    leagueid = models.IntegerField()
    teamid = models.IntegerField()
    drawid = models.IntegerField()
    points = models.IntegerField()
    lastcalc = models.PositiveIntegerField()
    previous = models.IntegerField()
    previouscalc = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'fantasypoints'


class Fantasypool(models.Model):
    poolid = models.AutoField(primary_key=True)
    pooltypeid = models.IntegerField()
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()
    pickslockeddate = models.PositiveIntegerField()
    poolname = models.CharField(max_length=100)
    active = models.IntegerField()
    sponsor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'fantasypool'


class Fantasyteam(models.Model):
    teamid = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    teamname = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'fantasyteam'


class Forum(models.Model):
    forumid = models.SmallAutoField(primary_key=True)
    styleid = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    active = models.SmallIntegerField()
    displayorder = models.SmallIntegerField()
    replycount = models.PositiveIntegerField()
    lastpost = models.IntegerField()
    lastposter = models.CharField(max_length=50)
    threadcount = models.PositiveIntegerField()
    allowposting = models.IntegerField()
    cancontainthreads = models.SmallIntegerField()
    sponsorname = models.CharField(max_length=100)
    sponsorimg = models.CharField(max_length=100)
    sponsorurl = models.CharField(max_length=255)
    daysprune = models.PositiveSmallIntegerField()
    newpostemail = models.CharField(max_length=250)
    newthreademail = models.CharField(max_length=250)
    moderatenew = models.SmallIntegerField()
    moderateattach = models.SmallIntegerField()
    allowbbcode = models.SmallIntegerField()
    allowimages = models.SmallIntegerField()
    allowhtml = models.SmallIntegerField()
    allowsmilies = models.SmallIntegerField()
    allowicons = models.SmallIntegerField()
    parentid = models.SmallIntegerField()
    parentlist = models.CharField(max_length=250)
    allowratings = models.SmallIntegerField()
    countposts = models.SmallIntegerField()
    styleoverride = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'forum'


class Forumpermission(models.Model):
    forumpermissionid = models.SmallAutoField(primary_key=True)
    forumid = models.PositiveSmallIntegerField()
    usergroupid = models.PositiveSmallIntegerField()
    canview = models.SmallIntegerField()
    cansearch = models.SmallIntegerField()
    canemail = models.SmallIntegerField()
    canpostnew = models.SmallIntegerField()
    canmove = models.SmallIntegerField()
    canopenclose = models.SmallIntegerField()
    candeletethread = models.SmallIntegerField()
    canreplyown = models.SmallIntegerField()
    canreplyothers = models.SmallIntegerField()
    canviewothers = models.SmallIntegerField()
    caneditpost = models.SmallIntegerField()
    candeletepost = models.SmallIntegerField()
    canpostattachment = models.SmallIntegerField()
    canpostpoll = models.SmallIntegerField()
    canvote = models.SmallIntegerField()
    cangetattachment = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'forumpermission'


class Forumskin(models.Model):
    forumskinid = models.IntegerField()
    forumid = models.IntegerField()
    skinurl = models.CharField(max_length=150)
    forumredirect = models.IntegerField()
    textareacols = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'forumskin'


class Gamereviews(models.Model):
    reviewid = models.AutoField(primary_key=True)
    gameid = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rating = models.IntegerField()
    gameplay = models.IntegerField()
    realism = models.IntegerField()
    lookandfeel = models.IntegerField()
    comments = models.TextField()
    dateposted = models.DateTimeField()
    admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gamereviews'


class Games(models.Model):
    gameid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.TextField()
    url = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    featured = models.IntegerField()
    date = models.DateTimeField()
    developer = models.CharField(max_length=50)
    type = models.IntegerField()
    downloadurl = models.CharField(max_length=100)
    purchaseurl = models.CharField(max_length=100)
    playurl = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'games'


class Gametype(models.Model):
    gametypeid = models.IntegerField(primary_key=True)
    gametype = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'gametype'


class Icon(models.Model):
    iconid = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    iconpath = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'icon'


class Imagegal(models.Model):
    imagegalid = models.AutoField(primary_key=True)
    postid = models.PositiveIntegerField()
    upimage = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    userid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'imagegal'


class Language(models.Model):
    langid = models.AutoField(primary_key=True)
    language = models.CharField(max_length=50)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'language'


class Leaguegame(models.Model):
    leaguegameid = models.AutoField(primary_key=True)
    tournamentid = models.IntegerField()
    weekid = models.IntegerField()
    gamedatetime = models.DateTimeField()
    locationid = models.IntegerField()
    teamid1 = models.IntegerField()
    teamid2 = models.IntegerField()
    flightid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'leaguegame'


class LinkTracker(models.Model):
    linkid = models.AutoField(primary_key=True)
    linktype = models.IntegerField()
    linkdate = models.IntegerField()
    linkname = models.CharField(max_length=255)
    linkurl = models.CharField(max_length=255)
    linkcount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'link_tracker'


class LinkTrackerVisit(models.Model):
    visitid = models.AutoField(primary_key=True)
    linkid = models.IntegerField()
    ipaddress = models.CharField(max_length=15)
    referrer = models.CharField(max_length=250)
    visitdate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'link_tracker_visit'


class List(models.Model):
    listid = models.AutoField(primary_key=True)
    listtitle = models.CharField(max_length=255)
    listdescription = models.TextField()
    listdate = models.IntegerField()
    listactive = models.IntegerField()
    photoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'list'


class ListSlide(models.Model):
    listslideid = models.AutoField(primary_key=True)
    slideid = models.IntegerField()
    listid = models.IntegerField()
    playerid = models.IntegerField()
    slidetitle = models.CharField(max_length=255)
    slidetext = models.TextField()
    slidecontent = models.TextField()
    photoid = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'list_slide'


class MediaAgateEventDraw(models.Model):
    agateid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    drawid = models.IntegerField()
    can_west = models.IntegerField()
    can_west_date = models.IntegerField()
    can_east = models.IntegerField()
    can_east_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'media_agate_event_draw'


class Medialist(models.Model):
    mediaid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=30)
    organization = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    email2 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    province = models.IntegerField()
    country = models.IntegerField()
    phone = models.CharField(max_length=30)
    emailsent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medialist'


class MedialistEventtype(models.Model):
    mediaid = models.IntegerField()
    eventtypeid = models.IntegerField()
    agate = models.IntegerField()
    news = models.IntegerField()
    emailsent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medialist_eventtype'


class Mediatype(models.Model):
    mediatypeid = models.IntegerField()
    title = models.CharField(max_length=20)
    country = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mediatype'


class Moderator(models.Model):
    moderatorid = models.SmallAutoField(primary_key=True)
    userid = models.PositiveIntegerField()
    forumid = models.SmallIntegerField()
    newthreademail = models.SmallIntegerField()
    newpostemail = models.SmallIntegerField()
    caneditposts = models.SmallIntegerField()
    candeleteposts = models.SmallIntegerField()
    canviewips = models.SmallIntegerField()
    canmanagethreads = models.SmallIntegerField()
    canopenclose = models.SmallIntegerField()
    caneditthreads = models.SmallIntegerField()
    caneditstyles = models.SmallIntegerField()
    canbanusers = models.SmallIntegerField()
    canviewprofile = models.SmallIntegerField()
    canannounce = models.SmallIntegerField()
    canmassmove = models.SmallIntegerField()
    canmassprune = models.SmallIntegerField()
    canmoderateposts = models.SmallIntegerField()
    canmoderateattachments = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'moderator'


class News(models.Model):
    category = models.IntegerField()
    category2 = models.IntegerField()
    date = models.DateField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    text = models.TextField()
    link = models.CharField(max_length=200)
    province = models.IntegerField()
    clubid = models.IntegerField()
    eventid = models.IntegerField()
    eventid2 = models.IntegerField()
    frontfeatured = models.IntegerField()
    categoryfeatured = models.IntegerField()
    frontnewsphotoid = models.IntegerField()
    description = models.TextField()
    title_french = models.CharField(max_length=255)
    author_french = models.CharField(max_length=100)
    description_french = models.TextField()
    text_french = models.TextField()
    imagewidth = models.IntegerField()
    release = models.IntegerField()
    french = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'news'


class Newslettertype(models.Model):
    newslettertypeid = models.CharField(max_length=10)
    eventtypeid = models.IntegerField()
    title = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'newslettertype'


class Newslink(models.Model):
    newslink_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=75)
    date = models.DateField()
    link = models.CharField(max_length=255)
    username = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'newslink'


class NewslinkPrize(models.Model):
    newslink_prize_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    week = models.IntegerField()
    iswinner = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'newslink_prize'


class Newsphoto(models.Model):
    newsphotoid = models.AutoField(primary_key=True)
    photopath = models.CharField(max_length=100)
    photocaption = models.CharField(max_length=255)
    photocaption_french = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'newsphoto'


class Notes(models.Model):
    noteid = models.AutoField(primary_key=True)
    datetime = models.IntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    source_name = models.CharField(max_length=100)
    source_link = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'notes'


class NotesEvent(models.Model):
    linkid = models.AutoField(primary_key=True)
    noteid = models.IntegerField()
    eventid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notes_event'


class NotesPlayer(models.Model):
    linkid = models.AutoField(primary_key=True)
    noteid = models.IntegerField()
    playerid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notes_player'


class NotesTeam(models.Model):
    linkid = models.AutoField(primary_key=True)
    noteid = models.IntegerField()
    profileid = models.IntegerField()
    eventtypeid = models.IntegerField()
    teamid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notes_team'


class OrderOfMeritCtrs(models.Model):
    ctrsid = models.AutoField(primary_key=True)
    regionid = models.IntegerField()
    teamid = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    week = models.IntegerField()
    points = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'order_of_merit_ctrs'


class OrderOfMeritCtrsList(models.Model):
    listid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    regionid = models.IntegerField()
    include_children = models.IntegerField()
    listname = models.CharField(max_length=100)
    listshort = models.CharField(max_length=10)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_ctrs_list'


class OrderOfMeritEventSfm(models.Model):
    sfmid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    sfmdate = models.IntegerField()
    sfmvalue = models.DecimalField(max_digits=7, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'order_of_merit_event_sfm'


class OrderOfMeritFactorImportance(models.Model):
    oomid = models.IntegerField()
    eventtypeid = models.IntegerField()
    level = models.IntegerField()
    regionid = models.IntegerField()
    importance_factor = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'order_of_merit_factor_importance'


class OrderOfMeritFactorMoney(models.Model):
    oomid = models.IntegerField()
    low_value = models.IntegerField()
    low_factor = models.DecimalField(max_digits=8, decimal_places=3)
    high_value = models.IntegerField()
    high_factor = models.DecimalField(max_digits=8, decimal_places=3)
    multiplier = models.DecimalField(max_digits=6, decimal_places=5)
    value_base = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_factor_money'


class OrderOfMeritFactorTeams(models.Model):
    oomid = models.IntegerField()
    low_value = models.IntegerField()
    low_factor = models.DecimalField(max_digits=7, decimal_places=4)
    high_value = models.IntegerField()
    high_factor = models.DecimalField(max_digits=8, decimal_places=3)
    multiplier = models.DecimalField(max_digits=6, decimal_places=5)
    value_base = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_factor_teams'


class OrderOfMeritList(models.Model):
    listid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    startyear = models.IntegerField()
    endyear = models.IntegerField()
    listname = models.CharField(max_length=255)
    listshort = models.CharField(max_length=10)
    category = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_list'


class OrderOfMeritListException(models.Model):
    listid = models.IntegerField()
    epochid = models.IntegerField()
    profileid = models.IntegerField()
    teamid = models.IntegerField()
    eventid = models.IntegerField()
    adjustment = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'order_of_merit_list_exception'


class OrderOfMeritListItem(models.Model):
    listid = models.IntegerField()
    epochid = models.IntegerField()
    profileid = models.IntegerField()
    teamid = models.IntegerField()
    eventyear = models.IntegerField()
    pointtotal = models.DecimalField(max_digits=8, decimal_places=3)
    adjustment = models.DecimalField(max_digits=8, decimal_places=3)
    adjustedtotal = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'order_of_merit_list_item'


class OrderOfMeritListRegional(models.Model):
    listid = models.AutoField(primary_key=True)
    listid_link = models.IntegerField()
    listname = models.CharField(max_length=50)
    listshort = models.CharField(max_length=8)
    sectionid = models.IntegerField()
    sub_section = models.IntegerField()
    eventyear = models.IntegerField()
    eventtypeid = models.IntegerField()
    use_oom_all = models.IntegerField()
    use_alternate = models.IntegerField()
    eventcount = models.IntegerField()
    eventcount_region = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_list_regional'


class OrderOfMeritListRegionalEvent(models.Model):
    listid = models.IntegerField()
    eventid = models.IntegerField()
    use_points_version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_list_regional_event'


class OrderOfMeritListRegionalPoints(models.Model):
    oomptid = models.AutoField(primary_key=True)
    listid = models.IntegerField()
    teamid = models.IntegerField()
    eventid = models.IntegerField()
    points = models.DecimalField(max_digits=7, decimal_places=4)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_list_regional_points'


class OrderOfMeritListRegionalSection(models.Model):
    listid = models.IntegerField()
    sectionid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_list_regional_section'


class OrderOfMeritListRegionalTeam(models.Model):
    listid = models.IntegerField()
    teamid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_list_regional_team'


class OrderOfMeritListTotal(models.Model):
    listid = models.IntegerField()
    epochid = models.IntegerField()
    teamid = models.IntegerField()
    pointtotal = models.DecimalField(max_digits=8, decimal_places=3)
    adjustment = models.DecimalField(max_digits=8, decimal_places=3)
    adjustedtotal = models.DecimalField(max_digits=8, decimal_places=3)
    dateline = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_list_total'


class OrderOfMeritPointsPerWin(models.Model):
    oomid = models.IntegerField()
    eventtypeid = models.IntegerField()
    level = models.IntegerField()
    ppw = models.DecimalField(max_digits=8, decimal_places=3)
    qualifier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_points_per_win'


class OrderOfMeritSfmSettings(models.Model):
    oomid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    sfm_max = models.DecimalField(max_digits=9, decimal_places=2)
    sfm_min = models.DecimalField(max_digits=9, decimal_places=2)
    sfm_scale = models.IntegerField()
    sfm_fixed = models.IntegerField()
    min_teams = models.IntegerField()
    event_count = models.IntegerField()
    topcount = models.IntegerField()
    toppercent = models.IntegerField()
    use_oom_status = models.IntegerField()
    toptencount = models.IntegerField()
    toptwentycount = models.IntegerField()
    count_zero_teams = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_sfm_settings'


class OrderOfMeritSfmTeamAdjustment(models.Model):
    eventid = models.IntegerField()
    teamid = models.IntegerField()
    sfm_value = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'order_of_merit_sfm_team_adjustment'


class OrderOfMeritSfmValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    startvalue = models.IntegerField()
    endvalue = models.IntegerField()
    pointvalue = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'order_of_merit_sfm_values'


class OrderOfMeritSubclient(models.Model):
    oomtypeid = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=100)
    regionid = models.IntegerField()
    directory = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'order_of_merit_subclient'


class OrderOfMeritSublist(models.Model):
    listid = models.AutoField(primary_key=True)
    oomtypeid = models.IntegerField()
    eventtypeid = models.IntegerField()
    coreid = models.IntegerField()
    sectionid = models.IntegerField()
    listname = models.CharField(max_length=100)
    listsub = models.CharField(max_length=5)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_sublist'


class OrderOfMeritSublistYear(models.Model):
    yid = models.AutoField(primary_key=True)
    oomtypeid = models.IntegerField()
    eventyear = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_sublist_year'


class OrderOfMeritTeam(models.Model):
    teamid = models.IntegerField()
    fiveplayerteam = models.IntegerField()
    oomtypeid = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    totalpoints = models.DecimalField(max_digits=8, decimal_places=3)
    teampoints = models.DecimalField(max_digits=8, decimal_places=3)
    teamage = models.IntegerField()
    skip = models.IntegerField()
    fourth = models.IntegerField()
    fourthpoints = models.DecimalField(max_digits=8, decimal_places=3)
    third = models.IntegerField()
    thirdpoints = models.DecimalField(max_digits=8, decimal_places=3)
    second = models.IntegerField()
    secondpoints = models.DecimalField(max_digits=8, decimal_places=3)
    lead = models.IntegerField()
    leadpoints = models.DecimalField(max_digits=8, decimal_places=3)
    spare = models.IntegerField()
    sparepoints = models.DecimalField(max_digits=8, decimal_places=3)
    modifier = models.DecimalField(max_digits=8, decimal_places=3)
    ctrs_registered = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_team'


class OrderOfMeritTeamPlayerAdjustment(models.Model):
    adjustmentid = models.AutoField(primary_key=True)
    oomtypeid = models.IntegerField()
    playerid = models.IntegerField()
    eventyear = models.IntegerField()
    adjustment = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'order_of_merit_team_player_adjustment'


class OrderOfMeritWeek(models.Model):
    teamid = models.IntegerField()
    playerid = models.IntegerField()
    position = models.IntegerField()
    oomtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventid = models.IntegerField()
    week = models.IntegerField()
    weekmoney = models.IntegerField()
    weekpoints = models.DecimalField(max_digits=8, decimal_places=3)
    lastyearpct = models.DecimalField(max_digits=8, decimal_places=3)
    modifier = models.DecimalField(max_digits=8, decimal_places=3)
    rank = models.IntegerField()
    ctrs_registered = models.IntegerField()
    pointtotal = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'order_of_merit_week'


class OrderOfMeritWeekSettings(models.Model):
    oomid = models.IntegerField()
    eventweek = models.IntegerField()
    lastyearpct = models.DecimalField(max_digits=9, decimal_places=2)
    eventcount = models.IntegerField()
    ctrscount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_of_merit_week_settings'


class Photos(models.Model):
    photoid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    galleryid = models.IntegerField()
    eventid = models.IntegerField()
    clubid = models.IntegerField()
    imgfile = models.CharField(max_length=50)
    imgsize = models.IntegerField()
    imgwidth = models.IntegerField()
    imgheight = models.IntegerField()
    imgthumb = models.CharField(max_length=50)
    imgoriginal = models.CharField(max_length=100)
    phototext = models.CharField(max_length=255)
    credit = models.CharField(max_length=200)
    status = models.IntegerField()
    count = models.IntegerField()
    orientation = models.IntegerField()
    champion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'photos'


class PhotosGallery(models.Model):
    galleryid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    clubid = models.IntegerField()
    gallery = models.CharField(max_length=150)
    description = models.TextField()
    private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'photos_gallery'


class PhotosPlayer(models.Model):
    photoid = models.IntegerField()
    playerid = models.IntegerField()
    userid = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photos_player'





class PlayerBio(models.Model):
    playerid = models.IntegerField()
    lastupdated = models.IntegerField()
    inownwords = models.TextField()
    highlights = models.TextField()
    juniors = models.TextField()
    inownwords_change = models.TextField()
    highlights_change = models.TextField()
    juniors_change = models.TextField()

    class Meta:
        managed = False
        db_table = 'player_bio'


class PlayerChange(models.Model):
    playerid = models.ForeignKey(Player, models.DO_NOTHING, db_column='playerid')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    borncity = models.CharField(max_length=100)
    bornprovince = models.IntegerField()
    homecity = models.CharField(max_length=100)
    homeprovince = models.IntegerField()
    birthdate = models.DateField()
    hide_birthdate = models.IntegerField()
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
    twitter = models.CharField(max_length=50)
    facebook = models.CharField(max_length=150)
    wikipedia = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'player_change'


class PlayerEmail(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_email'


class PlayerFamily(models.Model):
    familyid = models.IntegerField()
    playerid = models.ForeignKey(Player, models.DO_NOTHING, db_column='playerid')
    typeid = models.IntegerField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'player_family'


class PlayerFeature(models.Model):
    playerid = models.ForeignKey(Player, models.DO_NOTHING, db_column='playerid')
    photoid = models.IntegerField()
    categoryid = models.IntegerField()
    description = models.CharField(max_length=250)
    dateline = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_feature'


class PlayerHeadshot(models.Model):
    headshotid = models.IntegerField()
    userid = models.IntegerField()
    playerid = models.ForeignKey(Player, models.DO_NOTHING, db_column='playerid')
    email = models.CharField(max_length=50)
    imgfile = models.CharField(max_length=100)
    shortdesc = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'player_headshot'


class PlayerLooking(models.Model):
    playerid = models.ForeignKey(Player, models.DO_NOTHING, db_column='playerid')
    eventyear = models.IntegerField()
    teamtype = models.IntegerField()
    showemail = models.IntegerField()
    position = models.IntegerField()
    sectionid = models.IntegerField()
    comments = models.TextField()

    class Meta:
        managed = False
        db_table = 'player_looking'


class PlayerQuestion(models.Model):
    questionid = models.IntegerField()
    question = models.CharField(max_length=255)
    categoryid = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_question'


class PlayerQuestionAnswer(models.Model):
    playerquestionid = models.AutoField(primary_key=True)
    playerid = models.IntegerField()
    lastupdated = models.IntegerField()
    questionid = models.IntegerField()
    answer = models.TextField()
    answer_change = models.TextField()

    class Meta:
        managed = False
        db_table = 'player_question_answer'


class PlayerQuestionCategory(models.Model):
    categoryid = models.AutoField(primary_key=True)
    category = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'player_question_category'


class PlayerRankings(models.Model):
    playerid = models.ForeignKey(Player, models.DO_NOTHING, db_column='playerid')
    overall = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_rankings'


class PlayerSignup(models.Model):
    signupid = models.AutoField(primary_key=True)
    process = models.IntegerField()
    userid = models.IntegerField()
    eventtypeid = models.IntegerField()
    clubid = models.IntegerField()
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    province = models.IntegerField()
    email = models.CharField(max_length=255)
    birthdate = models.DateField()
    registered = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player_signup'


class Playermoney(models.Model):
    playerid = models.IntegerField()
    moneytotal = models.DecimalField(max_digits=8, decimal_places=2)
    pointtotal = models.DecimalField(max_digits=8, decimal_places=2)
    qualified = models.IntegerField()
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'playermoney'


class Poll(models.Model):
    pollid = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    dateline = models.PositiveIntegerField()
    options = models.TextField()
    votes = models.TextField()
    active = models.SmallIntegerField()
    numberoptions = models.PositiveSmallIntegerField()
    timeout = models.PositiveSmallIntegerField()
    multiple = models.PositiveSmallIntegerField()
    voters = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'poll'


class Pollvote(models.Model):
    pollvoteid = models.AutoField(primary_key=True)
    pollid = models.PositiveIntegerField()
    userid = models.PositiveIntegerField()
    votedate = models.PositiveIntegerField()
    voteoption = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'pollvote'


class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    threadid = models.PositiveIntegerField()
    username = models.CharField(max_length=50)
    userid = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    dateline = models.PositiveIntegerField()
    attachmentid = models.PositiveSmallIntegerField()
    pagetext = models.TextField()
    allowsmilie = models.SmallIntegerField()
    showsignature = models.SmallIntegerField()
    ipaddress = models.CharField(max_length=16)
    iconid = models.PositiveSmallIntegerField()
    visible = models.SmallIntegerField()
    edituserid = models.PositiveIntegerField()
    editdate = models.PositiveIntegerField()
    spam = models.IntegerField()
    gameid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'post'


class PostVerifier(models.Model):
    verifierid = models.IntegerField()
    codeline = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'post_verifier'


class Privatemessage(models.Model):
    privatemessageid = models.AutoField(primary_key=True)
    folderid = models.SmallIntegerField()
    userid = models.PositiveIntegerField()
    touserid = models.PositiveIntegerField()
    fromuserid = models.PositiveIntegerField()
    title = models.CharField(max_length=250)
    message = models.TextField()
    dateline = models.PositiveIntegerField()
    showsignature = models.SmallIntegerField()
    iconid = models.PositiveSmallIntegerField()
    messageread = models.SmallIntegerField()
    readtime = models.PositiveIntegerField()
    receipt = models.PositiveSmallIntegerField()
    deleteprompt = models.PositiveSmallIntegerField()
    multiplerecipients = models.PositiveSmallIntegerField()
    attachmentid = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'privatemessage'


class Profilefield(models.Model):
    profilefieldid = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    required = models.SmallIntegerField()
    hidden = models.SmallIntegerField()
    maxlength = models.SmallIntegerField()
    size = models.SmallIntegerField()
    displayorder = models.SmallIntegerField()
    editable = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'profilefield'


class Replacement(models.Model):
    replacementid = models.SmallAutoField(primary_key=True)
    replacementsetid = models.SmallIntegerField()
    findword = models.TextField()
    replaceword = models.TextField()

    class Meta:
        managed = False
        db_table = 'replacement'


class Replacementset(models.Model):
    replacementsetid = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'replacementset'


class Scoreadmin(models.Model):
    eventid = models.IntegerField()
    userid = models.IntegerField()
    adminlevel = models.IntegerField()
    admincontact = models.IntegerField()
    entrycontact = models.IntegerField()
    manager = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoreadmin'


class ScoreadminPermission(models.Model):
    permid = models.IntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'scoreadmin_permission'


class Scoreend(models.Model):
    gameid = models.IntegerField()
    teamid = models.IntegerField()
    teamid_event = models.IntegerField()
    inning = models.IntegerField()
    hammer = models.IntegerField()
    powerplay = models.IntegerField()
    score = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'scoreend'


class ScoreendUpdateSent(models.Model):
    gameid = models.IntegerField()
    teamid = models.IntegerField()
    inning = models.IntegerField()
    score = models.IntegerField()
    sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoreend_update_sent'


class Scorefinal(models.Model):
    gameid = models.IntegerField()
    tied = models.IntegerField()
    extra_end_game = models.IntegerField()
    winningteam = models.IntegerField()
    losingteam = models.IntegerField()
    winningscore = models.IntegerField()
    winningscore_hammer = models.IntegerField()
    losingscore = models.IntegerField()
    losingscore_hammer = models.IntegerField()
    winningpoints = models.IntegerField()
    losingpoints = models.IntegerField()
    winningends = models.IntegerField()
    winningends_hammer = models.IntegerField()
    losingends = models.IntegerField()
    losingends_hammer = models.IntegerField()
    blanks = models.IntegerField()
    winningblanks_hammer = models.IntegerField()
    winningtwos = models.IntegerField()
    winningtwos_hammer = models.IntegerField()
    losingtwos = models.IntegerField()
    losingtwos_hammer = models.IntegerField()
    winningthrees = models.IntegerField()
    winningthrees_hammer = models.IntegerField()
    losingthrees = models.IntegerField()
    losingthrees_hammer = models.IntegerField()
    winningfours = models.IntegerField()
    winningfours_hammer = models.IntegerField()
    losingfours = models.IntegerField()
    losingfours_hammer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scorefinal'


class ScorefinalUpdateSent(models.Model):
    gameid = models.IntegerField()
    winningteam = models.IntegerField()
    losingteam = models.IntegerField()
    winningscore = models.IntegerField()
    losingscore = models.IntegerField()
    sent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scorefinal_update_sent'


class Scoregame(models.Model):
    gameid = models.IntegerField(primary_key=True)
    drawid = models.IntegerField()
    teamid1 = models.IntegerField()
    teamid2 = models.IntegerField()
    teamid_top = models.IntegerField()
    teamid_bottom = models.IntegerField()
    profileid1 = models.IntegerField()
    profileid2 = models.IntegerField()
    hammer = models.IntegerField()
    numends = models.IntegerField()
    teamid1_colour = models.CharField(max_length=10)
    teamid2_colour = models.CharField(max_length=10)
    teamid1_draw = models.DecimalField(max_digits=9, decimal_places=2)
    teamid2_draw = models.DecimalField(max_digits=9, decimal_places=2)
    teamid1_draw_two = models.DecimalField(max_digits=9, decimal_places=2)
    teamid2_draw_two = models.DecimalField(max_digits=9, decimal_places=2)
    teamid1_draw_three = models.DecimalField(max_digits=9, decimal_places=2)
    teamid2_draw_three = models.DecimalField(max_digits=9, decimal_places=2)
    teamid1_draw_four = models.DecimalField(max_digits=9, decimal_places=2)
    teamid2_draw_four = models.DecimalField(max_digits=9, decimal_places=2)
    skipid1 = models.IntegerField()
    fourthid1 = models.IntegerField()
    thirdid1 = models.IntegerField()
    sectionid1 = models.IntegerField()
    skipid2 = models.IntegerField()
    fourthid2 = models.IntegerField()
    thirdid2 = models.IntegerField()
    sectionid2 = models.IntegerField()
    counter = models.IntegerField()
    local_gameid = models.IntegerField()
    fantasy_email = models.IntegerField()
    tweet_end_by_end = models.IntegerField()
    threadid = models.IntegerField()
    length = models.IntegerField()
    streamcount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame'


class ScoregameAdmin(models.Model):
    profileid = models.AutoField(primary_key=True)
    gameid = models.IntegerField()
    userid = models.IntegerField()
    teamid1_scoring = models.IntegerField()
    teamid1_checklist = models.IntegerField()
    teamid2_scoring = models.IntegerField()
    teamid2_checklist = models.IntegerField()
    formattype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_admin'


class ScoregameChecklist(models.Model):
    checkid = models.IntegerField()
    gameid = models.IntegerField()
    inning = models.IntegerField()
    check1 = models.IntegerField()
    check2 = models.IntegerField()
    check3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_checklist'


class ScoregameChecklistEnd(models.Model):
    endid = models.AutoField(primary_key=True)
    gameid = models.IntegerField()
    inning = models.IntegerField()
    teamid = models.IntegerField()
    hammer = models.IntegerField()
    shotnumber = models.IntegerField()
    scorecount = models.IntegerField()
    shotid = models.IntegerField()
    itemid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_checklist_end'


class ScoregameChecklistEndOption(models.Model):
    eoid = models.AutoField(primary_key=True)
    gameid = models.IntegerField()
    inning = models.IntegerField()
    shotnumber = models.IntegerField()
    shotid = models.IntegerField()
    optionid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_checklist_end_option'


class ScoregameChecklistShot(models.Model):
    shotid = models.IntegerField()
    shotname = models.CharField(max_length=25)
    description = models.CharField(max_length=155)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_checklist_shot'


class ScoregameChecklistShotItem(models.Model):
    itemid = models.IntegerField()
    shotid = models.IntegerField()
    itemname = models.CharField(max_length=25)
    zone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_checklist_shot_item'


class ScoregameChecklistShotOption(models.Model):
    optionid = models.IntegerField()
    shotid = models.IntegerField()
    optionname = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'scoregame_checklist_shot_option'


class ScoregameColour(models.Model):
    colourid = models.AutoField(primary_key=True)
    hexcode = models.CharField(max_length=10)
    colour = models.CharField(max_length=20)
    lightdark = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_colour'


class ScoregameLineup(models.Model):
    gamelineupid = models.AutoField(primary_key=True)
    gameid = models.IntegerField()
    userid = models.IntegerField()
    teamid1 = models.IntegerField()
    teamid2 = models.IntegerField()
    teamid1_skip = models.IntegerField()
    teamid1_fourth = models.IntegerField()
    teamid1_third = models.IntegerField()
    teamid1_second = models.IntegerField()
    teamid1_lead = models.IntegerField()
    teamid2_skip = models.IntegerField()
    teamid2_fourth = models.IntegerField()
    teamid2_third = models.IntegerField()
    teamid2_second = models.IntegerField()
    teamid2_lead = models.IntegerField()
    teamid1_isthree = models.IntegerField()
    teamid2_isthree = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_lineup'


class ScoregameTelevision(models.Model):
    tvid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    drawid = models.IntegerField()
    gameid = models.IntegerField()
    teamid = models.IntegerField()
    langid = models.IntegerField()
    accountname = models.CharField(max_length=100)
    gametime = models.IntegerField()
    gamecode = models.CharField(max_length=255)
    videotypeid = models.IntegerField()
    gamecodetwo = models.CharField(max_length=255)
    videotypeidtwo = models.IntegerField()
    details = models.TextField()
    embed_off = models.IntegerField()
    tier = models.IntegerField()
    priority = models.IntegerField()
    monetized = models.IntegerField()
    cards = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_television'


class ScoregameTelevisionAnalytics(models.Model):
    aid = models.AutoField(primary_key=True)
    tvid = models.IntegerField()
    length = models.IntegerField()
    peak = models.IntegerField()
    minutes = models.IntegerField()
    views3 = models.IntegerField()
    views10 = models.IntegerField()
    views60 = models.IntegerField()
    subscribers = models.IntegerField()
    revenue_estimate = models.DecimalField(max_digits=8, decimal_places=3)
    impressions = models.IntegerField()
    clickthrurate = models.DecimalField(max_digits=9, decimal_places=2)
    lastupdate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_television_analytics'


class ScoregameTelevisionAnalyticsImport(models.Model):
    gamecode = models.CharField(max_length=25)
    gametitle = models.CharField(max_length=100)
    publishdate = models.CharField(max_length=25)
    views = models.IntegerField()
    watchtime = models.DecimalField(max_digits=9, decimal_places=2)
    subscribers = models.IntegerField()
    revenue_estimate = models.DecimalField(max_digits=8, decimal_places=3)
    impressions = models.IntegerField()
    ctr = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'scoregame_television_analytics_import'


class ScoregameTelevisionEnd(models.Model):
    tvid = models.IntegerField()
    gameid = models.IntegerField()
    end = models.IntegerField()
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_television_end'


class ScoregameTelevisionOffice(models.Model):
    gameid = models.IntegerField()
    tvid = models.IntegerField()
    gigid = models.IntegerField()
    cid = models.IntegerField()
    allfeeds = models.IntegerField()
    thisfeed = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_television_office'


class ScoregameUpdateAudit(models.Model):
    time = models.IntegerField()
    userid = models.IntegerField()
    gameid = models.IntegerField()
    eventid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregame_update_audit'


class Scoregamehighlight(models.Model):
    ghid = models.AutoField(primary_key=True)
    gameid = models.IntegerField()
    endnumber = models.IntegerField()
    highlighttype = models.IntegerField()
    highlighttext = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'scoregamehighlight'


class Scoregameshot(models.Model):
    shotid = models.AutoField(primary_key=True)
    gameid = models.IntegerField()
    profileid = models.IntegerField()
    userid = models.IntegerField()
    eventid = models.IntegerField()
    teamid = models.IntegerField()
    playerid = models.IntegerField()
    inning = models.IntegerField()
    position = models.IntegerField()
    shotnumber = models.IntegerField()
    shottypeid = models.IntegerField()
    turn = models.IntegerField()
    track = models.IntegerField()
    modifier = models.IntegerField()
    count_teamid = models.IntegerField()
    count_total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregameshot'


class Scoregameshotinfo(models.Model):
    infoid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    shotid = models.IntegerField()
    turn = models.IntegerField()
    shottypeid = models.IntegerField()
    modifier = models.IntegerField()
    difficulty = models.DecimalField(max_digits=9, decimal_places=2)
    sweeping = models.IntegerField()
    sweeperror = models.IntegerField()
    pick = models.IntegerField()
    burn = models.IntegerField()
    skipsave = models.IntegerField()
    saveattempt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoregameshotinfo'


class Scoregameshotmodifier(models.Model):
    modifier = models.CharField(max_length=1)
    modifyname = models.CharField(max_length=25)
    shottype = models.IntegerField()
    prepost = models.IntegerField()
    bonus = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'scoregameshotmodifier'


class Scoregameshotscore(models.Model):
    scoreid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    shotid = models.IntegerField()
    score = models.IntegerField()
    difficulty = models.DecimalField(max_digits=5, decimal_places=4)
    sweeping = models.DecimalField(max_digits=9, decimal_places=2)
    modscore = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'scoregameshotscore'


class Scoregameshottype(models.Model):
    shottypeid = models.IntegerField()
    shotclass = models.IntegerField()
    shottype = models.CharField(max_length=25)
    rating = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'scoregameshottype'


class Scoreshort(models.Model):
    gameid = models.IntegerField()
    teamid = models.IntegerField()
    score = models.IntegerField()
    ends = models.IntegerField()
    blank = models.IntegerField()
    final = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoreshort'


class Search(models.Model):
    searchid = models.AutoField(primary_key=True)
    query = models.TextField()
    postids = models.TextField()
    dateline = models.PositiveIntegerField()
    querystring = models.CharField(max_length=200)
    showposts = models.SmallIntegerField()
    userid = models.PositiveIntegerField()
    ipaddress = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'search'


class Searchindex(models.Model):
    wordid = models.PositiveIntegerField()
    postid = models.PositiveIntegerField()
    intitle = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'searchindex'


class Section(models.Model):
    sectionid = models.IntegerField(primary_key=True)
    parent = models.IntegerField()
    level = models.IntegerField()
    section = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    plural = models.CharField(max_length=100)
    prefix = models.CharField(max_length=10)
    flag = models.CharField(max_length=15, blank=True, null=True)
    currency_name = models.CharField(max_length=50)
    currency = models.CharField(max_length=11)
    currency_code = models.CharField(max_length=5)
    timezoneid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'section'


class Session(models.Model):
    sessionhash = models.CharField(primary_key=True, max_length=32)
    userid = models.PositiveIntegerField()
    host = models.CharField(max_length=50)
    useragent = models.CharField(max_length=50)
    lastactivity = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    styleid = models.PositiveSmallIntegerField()
    tp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'session'


class Setting(models.Model):
    settingid = models.SmallAutoField(primary_key=True)
    settinggroupid = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    varname = models.CharField(max_length=100)
    value = models.TextField()
    description = models.TextField()
    optioncode = models.TextField()
    displayorder = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'setting'


class Settinggroup(models.Model):
    settinggroupid = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    displayorder = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'settinggroup'


class SimOrderOfMerit(models.Model):
    simid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit'


class SimOrderOfMeritBaseValues(models.Model):
    simid = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    tier = models.IntegerField()
    startvalue = models.IntegerField()
    endvalue = models.IntegerField()
    basevalue = models.DecimalField(max_digits=9, decimal_places=2)
    qualifier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_base_values'


class SimOrderOfMeritEvent(models.Model):
    simid = models.IntegerField()
    eventid = models.IntegerField()
    tourweek = models.IntegerField()
    strength_of_field = models.DecimalField(max_digits=9, decimal_places=2)
    oom_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_event'


class SimOrderOfMeritFactorImportance(models.Model):
    simid = models.IntegerField()
    eventtypeid = models.IntegerField()
    level = models.IntegerField()
    regionid = models.IntegerField()
    importance_factor = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_factor_importance'


class SimOrderOfMeritFactorMoney(models.Model):
    simid = models.IntegerField()
    low_value = models.IntegerField()
    low_factor = models.DecimalField(max_digits=8, decimal_places=3)
    high_value = models.IntegerField()
    high_factor = models.DecimalField(max_digits=8, decimal_places=3)
    multiplier = models.DecimalField(max_digits=6, decimal_places=5)
    value_base = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_factor_money'


class SimOrderOfMeritFactorTeams(models.Model):
    simid = models.IntegerField()
    low_value = models.IntegerField()
    low_factor = models.DecimalField(max_digits=8, decimal_places=3)
    high_value = models.IntegerField()
    high_factor = models.DecimalField(max_digits=8, decimal_places=3)
    multiplier = models.DecimalField(max_digits=6, decimal_places=5)
    value_base = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_factor_teams'


class SimOrderOfMeritPointsPerWin(models.Model):
    simid = models.IntegerField()
    eventtypeid = models.IntegerField()
    level = models.IntegerField()
    ppw = models.DecimalField(max_digits=8, decimal_places=3)
    qualifier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_points_per_win'


class SimOrderOfMeritSfmSettings(models.Model):
    simid = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    sfm_max = models.DecimalField(max_digits=9, decimal_places=2)
    sfm_min = models.DecimalField(max_digits=9, decimal_places=2)
    sfm_scale = models.IntegerField()
    sfm_fixed = models.IntegerField()
    min_teams = models.IntegerField()
    event_count = models.IntegerField()
    topcount = models.IntegerField()
    toppercent = models.IntegerField()
    use_oom_status = models.IntegerField()
    toptencount = models.IntegerField()
    toptwentycount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_sfm_settings'


class SimOrderOfMeritSfmTier(models.Model):
    simid = models.IntegerField()
    tierlevel = models.IntegerField()
    topeightcount = models.IntegerField()
    toptencount = models.IntegerField()
    toptwentycount = models.IntegerField()
    tierpoints = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_sfm_tier'


class SimOrderOfMeritSfmValues(models.Model):
    valueid = models.AutoField(primary_key=True)
    simid = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    startvalue = models.IntegerField()
    endvalue = models.IntegerField()
    pointvalue = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_sfm_values'


class SimOrderOfMeritTeam(models.Model):
    simid = models.IntegerField()
    teamid = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    totalpoints = models.DecimalField(max_digits=8, decimal_places=3)
    teampoints = models.DecimalField(max_digits=8, decimal_places=3)
    skip = models.IntegerField()
    fourth = models.IntegerField()
    fourthpoints = models.DecimalField(max_digits=8, decimal_places=3)
    third = models.IntegerField()
    thirdpoints = models.DecimalField(max_digits=8, decimal_places=3)
    second = models.IntegerField()
    secondpoints = models.DecimalField(max_digits=8, decimal_places=3)
    lead = models.IntegerField()
    leadpoints = models.DecimalField(max_digits=8, decimal_places=3)
    modifier = models.DecimalField(max_digits=8, decimal_places=3)
    ctrs_registered = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_team'


class SimOrderOfMeritWeek(models.Model):
    simid = models.IntegerField()
    teamid = models.IntegerField()
    eventyear = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventid = models.IntegerField()
    oom_status = models.IntegerField()
    week = models.IntegerField()
    weekmoney = models.IntegerField()
    weekpoints = models.DecimalField(max_digits=8, decimal_places=3)
    modifier = models.DecimalField(max_digits=8, decimal_places=3)
    rank = models.IntegerField()
    ctrs_registered = models.IntegerField()
    pointtotal = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'sim_order_of_merit_week'


class SimTeammoney(models.Model):
    eventid = models.IntegerField()
    simid = models.IntegerField()
    spielteamid = models.IntegerField()
    tourteamid = models.IntegerField()
    moneytotal = models.IntegerField()
    moneytotal_local = models.IntegerField()
    pointtotal = models.DecimalField(max_digits=8, decimal_places=3)
    pointtotal_base = models.DecimalField(max_digits=8, decimal_places=3)
    place = models.IntegerField()
    qualifier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sim_teammoney'


class Slide(models.Model):
    slideid = models.IntegerField()
    slideshowid = models.IntegerField()
    slidetitle = models.CharField(max_length=100)
    slidedescription = models.CharField(max_length=255)
    slidefilename = models.CharField(max_length=50)
    credit = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'slide'


class Slideshow(models.Model):
    slideshowid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    shortdesc = models.CharField(max_length=255)
    description = models.TextField()
    featured = models.IntegerField()
    slideshowdate = models.DateField()
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slideshow'


class Smilie(models.Model):
    smilieid = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    smilietext = models.CharField(max_length=10)
    smiliepath = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'smilie'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    id = models.BigAutoField(primary_key=True)
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class StadiumAdvertAsset(models.Model):
    assetid = models.AutoField(primary_key=True)
    asset = models.CharField(max_length=100)
    digital = models.IntegerField()
    type = models.IntegerField()
    measure = models.IntegerField()
    count_per_measure = models.IntegerField()
    measure_value = models.IntegerField()
    physical_revenue_per_measure = models.IntegerField()
    event_only = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_advert_asset'


class StadiumAdvertAssetTier(models.Model):
    atid = models.AutoField(primary_key=True)
    assetid = models.IntegerField()
    tierid = models.IntegerField()
    percent_of_measure = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_advert_asset_tier'


class StadiumAdvertAssetValue(models.Model):
    valueid = models.AutoField(primary_key=True)
    assetid = models.IntegerField()
    level = models.IntegerField()
    value = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'stadium_advert_asset_value'


class StadiumAdvertLevel(models.Model):
    levelid = models.AutoField(primary_key=True)
    label = models.CharField(max_length=25)
    description = models.TextField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_advert_level'


class StadiumAdvertMeasure(models.Model):
    itemid = models.AutoField(primary_key=True)
    item = models.CharField(max_length=25)
    label = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'stadium_advert_measure'


class StadiumAsset(models.Model):
    assetid = models.AutoField(primary_key=True)
    stadiumid = models.IntegerField()
    clubid = models.IntegerField()
    eventweekid = models.IntegerField()
    eventid = models.IntegerField()
    ptid = models.IntegerField()
    tier = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=3)
    cost = models.DecimalField(max_digits=8, decimal_places=3)
    asset_name = models.CharField(max_length=50)
    classid = models.IntegerField()
    measureid = models.IntegerField()
    count_per_measure = models.IntegerField()
    length = models.DecimalField(max_digits=9, decimal_places=2)
    asset_minutes = models.DecimalField(max_digits=8, decimal_places=3)
    impressions = models.IntegerField()
    tablevar = models.CharField(max_length=50)
    sold_as_group = models.IntegerField()
    sold_complete = models.IntegerField()
    team_sale = models.IntegerField()
    multiuse = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_asset'


class StadiumAssetClass(models.Model):
    classid = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_asset_class'


class StadiumAssetEvent(models.Model):
    aeid = models.AutoField(primary_key=True)
    assetid = models.IntegerField()
    stadiumid = models.IntegerField()
    clubid = models.IntegerField()
    eventid = models.IntegerField()
    teamid = models.IntegerField()
    socialid = models.IntegerField()
    eventweekid = models.IntegerField()
    tier = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=3)
    count_per_measure = models.IntegerField()
    length = models.IntegerField()
    asset_minutes = models.DecimalField(max_digits=12, decimal_places=3)
    total_minutes = models.IntegerField()
    impressions = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_asset_event'


class StadiumAssetGroup(models.Model):
    groupid = models.IntegerField(primary_key=True)
    groupname = models.CharField(max_length=100)
    stadium_active = models.IntegerField()
    event_active = models.IntegerField()
    status = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_asset_group'


class StadiumAssetGroupLink(models.Model):
    linkid = models.AutoField(primary_key=True)
    groupid = models.IntegerField()
    assetid = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_asset_group_link'


class StadiumAssetMeasure(models.Model):
    measureid = models.AutoField(primary_key=True)
    measure_name = models.CharField(max_length=100)
    minutes = models.IntegerField()
    game_default = models.IntegerField()
    per_year = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_asset_measure'


class StadiumAssetSale(models.Model):
    asid = models.AutoField(primary_key=True)
    aeid = models.IntegerField()
    supplierid = models.IntegerField()
    stadiumid = models.IntegerField()
    clubid = models.IntegerField()
    eventid = models.IntegerField()
    eventweekid = models.IntegerField()
    pricetype = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=3)
    price_per_mille = models.DecimalField(max_digits=8, decimal_places=3)
    itemcount = models.IntegerField()
    count_per_measure = models.DecimalField(max_digits=8, decimal_places=3)
    length = models.IntegerField()
    asset_minutes = models.DecimalField(max_digits=12, decimal_places=3)
    total_minutes = models.IntegerField()
    impressions = models.IntegerField()
    updated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_asset_sale'


class StadiumAssetSocial(models.Model):
    asid = models.AutoField(primary_key=True)
    assetid = models.IntegerField()
    eventid = models.IntegerField()
    socialid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_asset_social'


class StadiumBudgetSection(models.Model):
    bid = models.AutoField(primary_key=True)
    section_title = models.CharField(max_length=50)
    section_debit = models.IntegerField()
    section_priority = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_budget_section'


class StadiumClubsSheet(models.Model):
    ssid = models.AutoField(primary_key=True)
    sheetid = models.IntegerField()
    stadiumid = models.IntegerField()
    production_room = models.CharField(max_length=255)
    production_password = models.CharField(max_length=50)
    commentary_room = models.CharField(max_length=255)
    commentary_password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'stadium_clubs_sheet'


class StadiumCosts(models.Model):
    costid = models.AutoField(primary_key=True)
    stadium_setup = models.IntegerField()
    ptz_camera = models.IntegerField()
    fixed_camera = models.IntegerField()
    decoder = models.IntegerField()
    cables_per_sheet = models.IntegerField()
    monthly_sheet_fee = models.IntegerField()
    event_stream_revenues = models.IntegerField()
    events_per_cycle = models.IntegerField()
    revenue_per_game1 = models.IntegerField()
    revenue_per_game2 = models.IntegerField()
    birddog_discount = models.IntegerField()
    labour_cost_hour = models.IntegerField()
    tier1_labour_hours = models.IntegerField()
    tier2_labour_hours = models.IntegerField()
    tier3_labour_hours = models.IntegerField()
    team_marketing_tier1_price = models.IntegerField()
    team_marketing_tier2_price = models.IntegerField()
    team_marketing_tier3_price = models.IntegerField()
    team_games_default = models.IntegerField()
    usdcdn_exchange = models.FloatField()
    percent_ends_played_club = models.IntegerField()
    percent_ends_played_elite = models.IntegerField()
    minutes_per_end_club = models.IntegerField()
    minutes_per_end_elite = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_costs'


class StadiumEquipment(models.Model):
    equipid = models.AutoField(primary_key=True)
    supplierid = models.IntegerField()
    costid = models.IntegerField()
    ptid = models.IntegerField()
    itemname = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cost_retail = models.DecimalField(max_digits=9, decimal_places=2)
    cost_wholesale = models.DecimalField(max_digits=9, decimal_places=2)
    variable = models.IntegerField()
    currency = models.IntegerField()
    linkinfo = models.CharField(max_length=255)
    per_sheet = models.IntegerField()
    per_facility = models.IntegerField()
    optional = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_equipment'


class StadiumEquipmentClub(models.Model):
    ecid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    orderid = models.IntegerField()
    equipid = models.IntegerField()
    ownerid = models.IntegerField()
    pid = models.IntegerField()
    eid = models.IntegerField()
    status = models.IntegerField()
    updated_quote = models.IntegerField()
    updated_purchase = models.IntegerField()
    updated_install = models.IntegerField()
    updated_active = models.IntegerField()
    cost_retail = models.DecimalField(max_digits=9, decimal_places=2)
    cost_wholesale = models.DecimalField(max_digits=9, decimal_places=2)
    count = models.IntegerField()
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_equipment_club'


class StadiumEquipmentOrder(models.Model):
    orderid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    stadiumid = models.IntegerField()
    order_status = models.IntegerField()
    order_date = models.IntegerField()
    exchangerate = models.DecimalField(max_digits=6, decimal_places=5)
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'stadium_equipment_order'


class StadiumEquipmentOrderStatus(models.Model):
    order_status = models.IntegerField(primary_key=True)
    status_label = models.CharField(max_length=25)
    status_desc = models.CharField(max_length=25)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_equipment_order_status'


class StadiumEvent(models.Model):
    seid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    weekid = models.IntegerField()
    rr_games = models.IntegerField()
    rr_tier1 = models.IntegerField()
    rr_tier2 = models.IntegerField()
    tb_games = models.IntegerField()
    tb_tier1 = models.IntegerField()
    tb_tier2 = models.IntegerField()
    po_games = models.IntegerField()
    po_tier1 = models.IntegerField()
    po_tier2 = models.IntegerField()
    teams = models.IntegerField()
    all_draws = models.IntegerField()
    stadiumid = models.IntegerField()
    eventid = models.IntegerField()
    eventyear = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_event'


class StadiumEventDefault(models.Model):
    sedid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    event_description = models.TextField()
    org_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'stadium_event_default'


class StadiumEventKey(models.Model):
    skeyid = models.AutoField(primary_key=True)
    sktid = models.IntegerField()
    eventid = models.IntegerField()
    keylabel = models.CharField(max_length=100)
    keytext = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'stadium_event_key'


class StadiumEventKeyType(models.Model):
    sktid = models.AutoField(primary_key=True)
    keytype = models.TextField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_event_key_type'


class StadiumEventPartner(models.Model):
    epid = models.AutoField(primary_key=True)
    supplierid = models.IntegerField()
    stadiumid = models.IntegerField()
    eventid = models.IntegerField()
    commission = models.DecimalField(max_digits=8, decimal_places=2)
    revenue_share = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'stadium_event_partner'


class StadiumEventTierGames(models.Model):
    eventid = models.IntegerField()
    type = models.IntegerField()
    tierid = models.IntegerField()
    games = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_event_tier_games'


class StadiumEventTiers(models.Model):
    etid = models.AutoField(primary_key=True)
    tierid = models.IntegerField()
    eventyear = models.IntegerField()
    eventid = models.IntegerField()
    eventid_compare = models.IntegerField()
    eventweekid = models.IntegerField()
    aaviewers = models.IntegerField()
    averagewatch = models.IntegerField()
    value = models.IntegerField()
    discount = models.IntegerField()
    commercials = models.IntegerField()
    inlay = models.IntegerField()
    logos = models.IntegerField()
    logo_length = models.IntegerField()
    data_users = models.IntegerField()
    data_new_users = models.IntegerField()
    data_sessions = models.IntegerField()
    data_pageviews = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_event_tiers'


class StadiumEventType(models.Model):
    typeid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=25)
    description = models.TextField()
    event_days = models.IntegerField()
    playoff_games = models.IntegerField()
    ends = models.IntegerField()
    minutes_per_end = models.DecimalField(max_digits=9, decimal_places=2)
    percent_tier1_stream = models.IntegerField()
    percent_tier2_stream = models.IntegerField()
    percent_tier3_stream = models.IntegerField()
    percent_fixed_price = models.IntegerField()
    percent_ends_played = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_event_type'


class StadiumExpense(models.Model):
    expenseid = models.AutoField(primary_key=True)
    stadiumid = models.IntegerField()
    clubid = models.IntegerField()
    eventweekid = models.IntegerField()
    eventid = models.IntegerField()
    ptid = models.IntegerField()
    equipid = models.IntegerField()
    tier = models.IntegerField()
    expense_name = models.CharField(max_length=50)
    price = models.IntegerField()
    measureid = models.IntegerField()
    count_per_measure = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_expense'


class StadiumExpenseItem(models.Model):
    eid = models.IntegerField()
    expenseid = models.IntegerField()
    stadiumid = models.IntegerField()
    clubid = models.IntegerField()
    eventid = models.IntegerField()
    socialid = models.IntegerField()
    eventweekid = models.IntegerField()
    tier = models.IntegerField()
    cost = models.DecimalField(max_digits=8, decimal_places=3)
    itemcount = models.IntegerField()
    count_per_measure = models.IntegerField()
    totalcost = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'stadium_expense_item'


class StadiumGameAsset(models.Model):
    sgid = models.AutoField(primary_key=True)
    assetid = models.IntegerField()
    gameid = models.IntegerField()
    value = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'stadium_game_asset'


class StadiumGig(models.Model):
    gigid = models.AutoField(primary_key=True)
    gigname = models.CharField(max_length=50)
    gigdesc = models.TextField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_gig'


class StadiumGigLevel(models.Model):
    glid = models.AutoField(primary_key=True)
    gigid = models.IntegerField()
    level = models.IntegerField()
    rate_default = models.DecimalField(max_digits=8, decimal_places=2)
    ratetype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_gig_level'


class StadiumGigRole(models.Model):
    roleid = models.AutoField(primary_key=True)
    gigid = models.IntegerField()
    roletitle = models.CharField(max_length=50)
    roledescription = models.TextField()

    class Meta:
        managed = False
        db_table = 'stadium_gig_role'


class StadiumHome(models.Model):
    homeid = models.AutoField(primary_key=True)
    sectionid = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.IntegerField()
    country = models.IntegerField()
    postalcode = models.TextField()
    paymentdetails = models.TextField()
    priority = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_home'


class StadiumOffice(models.Model):
    cid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_office'


class StadiumOfficeGig(models.Model):
    ogid = models.AutoField(primary_key=True)
    cid = models.IntegerField()
    gigid = models.IntegerField()
    level = models.IntegerField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    ratetype = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_office_gig'


class StadiumPayment(models.Model):
    pid = models.AutoField(primary_key=True)
    ptid = models.IntegerField()
    debit = models.IntegerField()
    stadiumid = models.IntegerField()
    supplierid = models.IntegerField()
    aeid = models.IntegerField()
    groupid = models.IntegerField()
    eventid = models.IntegerField()
    teamid = models.IntegerField()
    datedue = models.IntegerField()
    status = models.IntegerField()
    updated = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=0)
    localcurrency = models.IntegerField()
    taxes = models.DecimalField(max_digits=10, decimal_places=0)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    contract = models.IntegerField()
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'stadium_payment'


class StadiumPaymentType(models.Model):
    ptid = models.AutoField(primary_key=True)
    bid = models.IntegerField()
    paymenttype = models.CharField(max_length=100)
    measureid = models.IntegerField()
    default_per_measure = models.DecimalField(max_digits=9, decimal_places=2)
    recurring = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_payment_type'


class StadiumPlaylist(models.Model):
    playlistid = models.AutoField(primary_key=True)
    eventid = models.IntegerField()
    productionid = models.IntegerField()
    gameid = models.IntegerField()
    tvid = models.IntegerField()
    playlist = models.CharField(max_length=50)
    length_opening = models.IntegerField()
    length_endbreak = models.IntegerField()
    length_closing = models.IntegerField()
    locked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_playlist'


class StadiumPlaylistEnd(models.Model):
    peid = models.AutoField(primary_key=True)
    playlistid = models.IntegerField()
    afterend = models.IntegerField()
    mediaid = models.IntegerField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_playlist_end'


class StadiumPlaylistTier(models.Model):
    linkid = models.AutoField(primary_key=True)
    playlistid = models.IntegerField()
    tierid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_playlist_tier'


class StadiumProduction(models.Model):
    productionid = models.AutoField(primary_key=True)
    production_date = models.IntegerField()
    dpid = models.IntegerField()
    tierid = models.IntegerField()
    eventid = models.IntegerField()
    playlistid = models.IntegerField()
    gamecount = models.IntegerField()
    roundid = models.IntegerField()
    drawid = models.IntegerField()
    gameid = models.IntegerField()
    production = models.CharField(max_length=50)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_production'


class StadiumProductionPart(models.Model):
    dpid = models.AutoField(primary_key=True)
    partlabel = models.CharField(max_length=10)
    partstart = models.IntegerField()
    partend = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_production_part'


class StadiumProductionRole(models.Model):
    prid = models.AutoField(primary_key=True)
    productionid = models.IntegerField()
    roleid = models.IntegerField()
    contractorid = models.IntegerField()
    payrate = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.IntegerField()
    paiddate = models.IntegerField()
    rolelock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_production_role'


class StadiumProductionRoleApplication(models.Model):
    praid = models.AutoField(primary_key=True)
    prid = models.IntegerField()
    contractorid = models.IntegerField()
    notes = models.TextField()
    status = models.IntegerField()
    waitlist = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_production_role_application'


class StadiumProductionRoleTier(models.Model):
    prtid = models.AutoField(primary_key=True)
    tierid = models.IntegerField()
    roleid = models.IntegerField()
    payrate = models.DecimalField(max_digits=9, decimal_places=2)
    currency = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_production_role_tier'


class StadiumSetup(models.Model):
    setupid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    stadiumid = models.IntegerField()
    structureid = models.IntegerField()
    stadium_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    contact_title = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    stadium_title = models.CharField(max_length=50)
    stadium_sheets = models.IntegerField()
    months_active = models.IntegerField()
    ptz = models.IntegerField()
    fixed = models.IntegerField()
    cycles = models.IntegerField()
    equipmentfee = models.IntegerField()
    managementfee = models.IntegerField()
    currency = models.IntegerField()
    notes = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_setup'


class StadiumSetupStructure(models.Model):
    structureid = models.IntegerField(primary_key=True)
    structure = models.CharField(max_length=25)
    structure_desc = models.CharField(max_length=100)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_setup_structure'


class StadiumSponsor(models.Model):
    sponsorid = models.AutoField(primary_key=True)
    supplierid = models.IntegerField()
    active = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_sponsor'


class StadiumSponsorAsset(models.Model):
    ssid = models.AutoField(primary_key=True)
    sponsor = models.CharField(max_length=50)
    stadiumid = models.IntegerField()
    eventid = models.IntegerField()
    groupid = models.IntegerField()
    assetid = models.IntegerField()
    updated = models.IntegerField()
    value_committed = models.DecimalField(max_digits=9, decimal_places=2)
    value_collected = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'stadium_sponsor_asset'


class StadiumSponsorDefault(models.Model):
    sdid = models.AutoField(primary_key=True)
    mediatype = models.IntegerField()
    media_length = models.IntegerField()
    market_price = models.DecimalField(max_digits=8, decimal_places=3)
    stadium_rate = models.DecimalField(max_digits=8, decimal_places=3)
    currency = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'stadium_sponsor_default'


class StadiumSponsorLink(models.Model):
    linkid = models.AutoField(primary_key=True)
    sponsorid = models.IntegerField()
    eventid = models.IntegerField()
    profileid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_sponsor_link'


class StadiumSponsorMedia(models.Model):
    mediaid = models.AutoField(primary_key=True)
    sponsorid = models.IntegerField()
    mediatype = models.IntegerField()
    length = models.IntegerField()
    driveurl = models.CharField(max_length=150)
    czfilename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'stadium_sponsor_media'


class StadiumSponsorMediaLink(models.Model):
    linkid = models.AutoField(primary_key=True)
    mediaid = models.IntegerField()
    eventid = models.IntegerField()
    profileid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_sponsor_media_link'


class StadiumSponsorQuote(models.Model):
    quoteid = models.AutoField(primary_key=True)
    sponsorid = models.IntegerField()
    eventid = models.IntegerField()
    sdid = models.IntegerField()
    gamecount = models.IntegerField()
    plays_per_game = models.IntegerField()
    plays_per_event = models.IntegerField()
    market_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=9, decimal_places=2)
    totalcost = models.DecimalField(max_digits=9, decimal_places=2)
    views_per_game = models.IntegerField()
    currency = models.IntegerField()
    quote_created = models.IntegerField()
    quote_updated = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_sponsor_quote'


class StadiumStreamMetrics(models.Model):
    metricid = models.AutoField(primary_key=True)
    entityid = models.IntegerField()
    dataset = models.CharField(max_length=50)
    airtime = models.IntegerField()
    views = models.IntegerField()
    minutes = models.IntegerField()
    impressions = models.IntegerField()
    ctr = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'stadium_stream_metrics'


class StadiumStreamTiers(models.Model):
    tierid = models.AutoField(primary_key=True)
    tiername = models.CharField(max_length=100)
    tierdescription = models.TextField()
    tiernickname = models.TextField()
    eventgamefee = models.DecimalField(max_digits=9, decimal_places=2)
    logo = models.IntegerField()
    videos = models.IntegerField()
    inlay = models.IntegerField()
    basetier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_stream_tiers'


class StadiumSupplier(models.Model):
    supplierid = models.AutoField(primary_key=True)
    clubid = models.IntegerField()
    teamid = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    provinceid = models.IntegerField()
    countryid = models.IntegerField()
    postalcode = models.CharField(max_length=20)
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'stadium_supplier'


class StadiumTeam(models.Model):
    stid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    sponsors = models.IntegerField()
    fees = models.IntegerField()
    games = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_team'


class StadiumWeek(models.Model):
    weekid = models.IntegerField()
    eventyear = models.IntegerField()
    startdate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stadium_week'


class Statistic(models.Model):
    teamid = models.IntegerField()
    categoryid = models.IntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=4)
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'statistic'


class StatisticCategory(models.Model):
    categoryid = models.IntegerField()
    parent = models.IntegerField()
    category = models.CharField(max_length=50)
    short = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    priority = models.IntegerField()
    format = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'statistic_category'


class Style(models.Model):
    styleid = models.SmallAutoField(primary_key=True)
    replacementsetid = models.PositiveSmallIntegerField()
    templatesetid = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=250)
    userselect = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'style'


class Subscribeforum(models.Model):
    subscribeforumid = models.AutoField(primary_key=True)
    userid = models.PositiveIntegerField()
    forumid = models.PositiveSmallIntegerField()
    emailupdate = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'subscribeforum'


class Subscribethread(models.Model):
    subscribethreadid = models.AutoField(primary_key=True)
    userid = models.PositiveIntegerField()
    threadid = models.PositiveIntegerField()
    emailupdate = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'subscribethread'


class Survey(models.Model):
    surveyid = models.AutoField(primary_key=True)
    skinid = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventid = models.IntegerField()
    surveyname = models.CharField(max_length=100)
    description = models.TextField()
    dateadded = models.DateField()
    datestart = models.DateField()
    dateend = models.DateField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'survey'


class Surveyage(models.Model):
    surveyageid = models.IntegerField()
    surveyid = models.IntegerField()
    age = models.CharField(max_length=10)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'surveyage'


class Surveyoption(models.Model):
    optionid = models.IntegerField()
    questionid = models.IntegerField()
    optionname = models.CharField(max_length=255)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'surveyoption'


class Surveyquestion(models.Model):
    questionid = models.AutoField(primary_key=True)
    sectionid = models.IntegerField()
    priority = models.IntegerField()
    question = models.CharField(max_length=255)
    questiontype = models.IntegerField()
    addcomments = models.IntegerField()
    required = models.IntegerField()
    selectmax = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'surveyquestion'


class Surveyquestionanswer(models.Model):
    takerid = models.IntegerField()
    questionid = models.IntegerField()
    questionanswer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'surveyquestionanswer'


class Surveyquestiontype(models.Model):
    questiontypeid = models.IntegerField()
    questiontype = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'surveyquestiontype'


class Surveysection(models.Model):
    sectionid = models.AutoField(primary_key=True)
    surveyid = models.IntegerField()
    sectionname = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'surveysection'


class Surveytaker(models.Model):
    takerid = models.AutoField(primary_key=True)
    surveyid = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    ipaddress = models.CharField(max_length=15)
    email = models.CharField(max_length=255, blank=True, null=True)
    takersex = models.IntegerField()
    takerage = models.IntegerField()
    datetaken = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'surveytaker'


class TalkTaboolaSettings(models.Model):
    publisher_id = models.CharField(max_length=255, blank=True, null=True)
    first_bc_enabled = models.IntegerField()
    first_bc_widget_id = models.CharField(max_length=255, blank=True, null=True)
    first_bc_custom_css = models.TextField(blank=True, null=True)
    second_bc_enabled = models.IntegerField()
    second_bc_widget_id = models.CharField(max_length=255, blank=True, null=True)
    second_bc_custom_css = models.TextField(blank=True, null=True)
    location_string = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk__taboola_settings'


class TalkCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_commentmeta'


class TalkComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.PositiveBigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'talk_comments'


class TalkCptchImages(models.Model):
    name = models.CharField(max_length=100)
    package_id = models.IntegerField()
    number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'talk_cptch_images'


class TalkCptchPackages(models.Model):
    name = models.CharField(max_length=100)
    folder = models.CharField(max_length=100)
    settings = models.TextField()
    user_settings = models.TextField()
    add_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'talk_cptch_packages'


class TalkCptchWhitelist(models.Model):
    ip = models.CharField(unique=True, max_length=31)
    ip_from_int = models.BigIntegerField(blank=True, null=True)
    ip_to_int = models.BigIntegerField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_cptch_whitelist'


class TalkLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.PositiveBigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'talk_links'


class TalkOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191, blank=True, null=True)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'talk_options'


class TalkPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_postmeta'


class TalkPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.PositiveBigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.PositiveBigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'talk_posts'


class TalkTermRelationships(models.Model):
    object_id = models.PositiveBigIntegerField(primary_key=True)
    term_taxonomy_id = models.PositiveBigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'talk_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class TalkTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.PositiveBigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'talk_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class TalkTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_termmeta'


class TalkTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'talk_terms'


class TalkUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_usermeta'


class TalkUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'talk_users'


class TalkWoocommerceApiKeys(models.Model):
    key_id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    description = models.CharField(max_length=200, blank=True, null=True)
    permissions = models.CharField(max_length=10)
    consumer_key = models.CharField(max_length=64)
    consumer_secret = models.CharField(max_length=43)
    nonces = models.TextField(blank=True, null=True)
    truncated_key = models.CharField(max_length=7)
    last_access = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_api_keys'


class TalkWoocommerceAttributeTaxonomies(models.Model):
    attribute_id = models.BigAutoField(primary_key=True)
    attribute_name = models.CharField(max_length=200)
    attribute_label = models.CharField(max_length=200, blank=True, null=True)
    attribute_type = models.CharField(max_length=20)
    attribute_orderby = models.CharField(max_length=20)
    attribute_public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_attribute_taxonomies'


class TalkWoocommerceDownloadableProductPermissions(models.Model):
    permission_id = models.BigAutoField(primary_key=True)
    download_id = models.CharField(max_length=32)
    product_id = models.PositiveBigIntegerField()
    order_id = models.PositiveBigIntegerField()
    order_key = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    downloads_remaining = models.CharField(max_length=9, blank=True, null=True)
    access_granted = models.DateTimeField()
    access_expires = models.DateTimeField(blank=True, null=True)
    download_count = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_downloadable_product_permissions'


class TalkWoocommerceLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    level = models.SmallIntegerField()
    source = models.CharField(max_length=200)
    message = models.TextField()
    context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_log'


class TalkWoocommerceOrderItemmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    order_item_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_order_itemmeta'


class TalkWoocommerceOrderItems(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order_item_name = models.TextField()
    order_item_type = models.CharField(max_length=200)
    order_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_order_items'


class TalkWoocommercePaymentTokenmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    payment_token_id = models.PositiveBigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_payment_tokenmeta'


class TalkWoocommercePaymentTokens(models.Model):
    token_id = models.BigAutoField(primary_key=True)
    gateway_id = models.CharField(max_length=200)
    token = models.TextField()
    user_id = models.PositiveBigIntegerField()
    type = models.CharField(max_length=200)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_payment_tokens'


class TalkWoocommerceSessions(models.Model):
    session_id = models.BigAutoField(unique=True)
    session_key = models.CharField(primary_key=True, max_length=32)
    session_value = models.TextField()
    session_expiry = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_sessions'


class TalkWoocommerceShippingZoneLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    zone_id = models.PositiveBigIntegerField()
    location_code = models.CharField(max_length=200)
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_shipping_zone_locations'


class TalkWoocommerceShippingZoneMethods(models.Model):
    zone_id = models.PositiveBigIntegerField()
    instance_id = models.BigAutoField(primary_key=True)
    method_id = models.CharField(max_length=200)
    method_order = models.PositiveBigIntegerField()
    is_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_shipping_zone_methods'


class TalkWoocommerceShippingZones(models.Model):
    zone_id = models.BigAutoField(primary_key=True)
    zone_name = models.CharField(max_length=200)
    zone_order = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_shipping_zones'


class TalkWoocommerceTaxRateLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_code = models.CharField(max_length=200)
    tax_rate_id = models.PositiveBigIntegerField()
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_tax_rate_locations'


class TalkWoocommerceTaxRates(models.Model):
    tax_rate_id = models.BigAutoField(primary_key=True)
    tax_rate_country = models.CharField(max_length=2)
    tax_rate_state = models.CharField(max_length=200)
    tax_rate = models.CharField(max_length=8)
    tax_rate_name = models.CharField(max_length=200)
    tax_rate_priority = models.PositiveBigIntegerField()
    tax_rate_compound = models.IntegerField()
    tax_rate_shipping = models.IntegerField()
    tax_rate_order = models.PositiveBigIntegerField()
    tax_rate_class = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'talk_woocommerce_tax_rates'





class TeamBlog(models.Model):
    teamblogid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    blogrss = models.CharField(max_length=150)
    userid = models.IntegerField()
    dateupdated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_blog'


class TeamEpoch(models.Model):
    epochid = models.AutoField(primary_key=True)
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_epoch'


class TeamEpochProfile(models.Model):
    tepid = models.AutoField(primary_key=True)
    epochid = models.IntegerField()
    profileid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_epoch_profile'


class TeamGame(models.Model):
    gameid = models.IntegerField()
    teamid = models.IntegerField()
    endchange = models.IntegerField()
    skip = models.IntegerField()
    fourth = models.IntegerField()
    third = models.IntegerField()
    second = models.IntegerField()
    lead = models.IntegerField()
    spare = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'team_game'


class TeamLayout(models.Model):
    layoutid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    profileid = models.IntegerField()
    eventyear = models.IntegerField()
    siteid = models.IntegerField()
    placeid = models.IntegerField()
    filename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'team_layout'


class TeamLayoutFont(models.Model):
    fontid = models.AutoField(primary_key=True)
    siteid = models.IntegerField()
    teamid = models.IntegerField()
    profileid = models.IntegerField()
    font_main = models.CharField(max_length=10)
    font_menu_on = models.CharField(max_length=10)
    background_menu_on = models.CharField(max_length=10)
    font_menu_off = models.CharField(max_length=10)
    background_menu_off = models.CharField(max_length=10)
    show_flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_layout_font'


class TeamLayoutPlacement(models.Model):
    placeid = models.AutoField(primary_key=True)
    siteid = models.IntegerField()
    placement = models.CharField(max_length=50)
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_layout_placement'


class TeamLayoutSite(models.Model):
    siteid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    eventtypeid2 = models.IntegerField()
    sitename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'team_layout_site'


class TeamNews(models.Model):
    linkid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    postid = models.IntegerField()
    type = models.IntegerField()
    featured = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_news'


class TeamPhoto(models.Model):
    photoid = models.IntegerField()
    teamid = models.IntegerField()
    profileid = models.IntegerField()
    userid = models.IntegerField()
    user_submitted = models.IntegerField()
    mainphoto = models.IntegerField()
    eventphoto = models.IntegerField()
    transfer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_photo'


class TeamPhotoProfile(models.Model):
    profileid = models.AutoField(primary_key=True)
    eventyear = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_photo_profile'


class TeamPhotoTeam(models.Model):
    teamid = models.IntegerField()
    profileid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_photo_team'


class TeamProfileEvent(models.Model):
    profileid = models.IntegerField()
    teamid = models.IntegerField()
    eventid = models.IntegerField()
    admin = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_profile_event'


class TeamPromote(models.Model):
    pid = models.AutoField(primary_key=True)
    profileid = models.IntegerField()
    promoteid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_promote'


class TeamPromoteLink(models.Model):
    linkid = models.IntegerField()
    eventtypeid = models.IntegerField()
    linkname = models.CharField(max_length=255)
    linkurl = models.CharField(max_length=255)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_promote_link'


class TeamPromoteSent(models.Model):
    promoteid = models.IntegerField()
    teamid = models.IntegerField()
    userid = models.IntegerField()
    tweet = models.CharField(max_length=150)
    message = models.CharField(max_length=150)
    hashtags = models.CharField(max_length=50)
    linkid = models.IntegerField()
    urlshort = models.CharField(max_length=50)
    datesent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_promote_sent'


class TeamPromoteTeam(models.Model):
    promoteid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    eventyear = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_promote_team'


class TeamPromoteTwitter(models.Model):
    promoteid = models.IntegerField(primary_key=True)
    twitter = models.TextField()
    consumerkey = models.TextField(db_column='consumerKey')  # Field name made lowercase.
    consumersecret = models.TextField(db_column='consumerSecret')  # Field name made lowercase.
    oauthtoken = models.TextField(db_column='oAuthToken')  # Field name made lowercase.
    oauthsecret = models.TextField(db_column='oAuthSecret')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'team_promote_twitter'


class TeamSignup(models.Model):
    signupid = models.AutoField(primary_key=True)
    eventtypeid = models.IntegerField()
    eventyear = models.IntegerField()
    eventid = models.IntegerField()
    drawid = models.IntegerField()
    status = models.IntegerField()
    fiveplayerteam = models.IntegerField()
    dateline = models.IntegerField()
    teamname = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.IntegerField()
    clubid = models.IntegerField()
    callsgame = models.IntegerField()
    fourthfirstname = models.CharField(max_length=255)
    fourthlastname = models.CharField(max_length=255)
    fourthemail = models.CharField(max_length=100)
    fourthplayerid = models.IntegerField()
    thirdfirstname = models.CharField(max_length=255)
    thirdlastname = models.CharField(max_length=255)
    thirdemail = models.CharField(max_length=100)
    thirdplayerid = models.IntegerField()
    secondfirstname = models.CharField(max_length=255)
    secondlastname = models.CharField(max_length=255)
    secondemail = models.CharField(max_length=100)
    secondplayerid = models.IntegerField()
    leadfirstname = models.CharField(max_length=255)
    leadlastname = models.CharField(max_length=255)
    leademail = models.CharField(max_length=100)
    leadplayerid = models.IntegerField()
    sparefirstname = models.CharField(max_length=255)
    sparelastname = models.CharField(max_length=255)
    spareemail = models.CharField(max_length=100)
    spareplayerid = models.IntegerField()
    coachfirstname = models.CharField(max_length=100)
    coachlastname = models.CharField(max_length=100)
    coachemail = models.CharField(max_length=100)
    coachplayerid = models.IntegerField()
    submittedby = models.CharField(max_length=255)
    submittedemail = models.CharField(max_length=255)
    userid = models.IntegerField()
    notes = models.TextField()
    fourth_birthdate = models.DateField()
    third_birthdate = models.DateField()
    second_birthdate = models.DateField()
    lead_birthdate = models.DateField()

    class Meta:
        managed = False
        db_table = 'team_signup'


class TeamSignupEventType(models.Model):
    signupid = models.IntegerField()
    eventtypeid = models.IntegerField()
    eventid = models.IntegerField()
    drawid = models.IntegerField()
    status = models.IntegerField()
    ctrs = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_signup_event_type'


class TeamSponsor(models.Model):
    sponsorid = models.IntegerField(primary_key=True)
    profileid = models.IntegerField()
    teamid = models.IntegerField()
    sponsorname = models.CharField(max_length=100)
    sponsordescription = models.TextField()
    sponsorurl = models.CharField(max_length=255)
    sponsorimage = models.CharField(max_length=100)
    sponsorthumb = models.CharField(max_length=100)
    priority = models.IntegerField()
    featured = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_sponsor'


class TeamSponsorProfile(models.Model):
    profileid = models.AutoField(primary_key=True)
    eventyear = models.IntegerField()
    web = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_sponsor_profile'


class TeamSponsorTeam(models.Model):
    tstid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    profileid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_sponsor_team'


class TeamSponsorUser(models.Model):
    sponsoruserid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    profileid = models.IntegerField()
    teamid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_sponsor_user'


class TeamStreamingLink(models.Model):
    tsid = models.AutoField(primary_key=True)
    profileid = models.IntegerField()
    linkname = models.CharField(max_length=100)
    videotypeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_streaming_link'


class TeamWaitinglist(models.Model):
    teamid = models.IntegerField(primary_key=True)
    eventid = models.IntegerField()
    eventtypeid = models.IntegerField()
    tier = models.IntegerField()
    drawid = models.IntegerField()
    status = models.IntegerField()
    fiveplayerteam = models.IntegerField()
    skip = models.IntegerField()
    fourth = models.IntegerField()
    third = models.IntegerField()
    second = models.IntegerField()
    lead = models.IntegerField()
    spare = models.IntegerField()
    coach = models.IntegerField()
    website = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    sectionid = models.IntegerField()
    clubid = models.IntegerField()
    teamname = models.CharField(max_length=100)
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
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'team_waitinglist'


class TeamWinningstreak(models.Model):
    streakid = models.AutoField(primary_key=True)
    teamid = models.IntegerField()
    eventyear = models.IntegerField()
    eventtypeid = models.IntegerField()
    streakcount = models.IntegerField()
    streakstart = models.IntegerField()
    streakstart_gametime = models.IntegerField()
    streakend = models.IntegerField()
    streakend_gametime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_winningstreak'


class Teamadmin(models.Model):
    teamid = models.IntegerField()
    userid = models.IntegerField()
    adminlevel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teamadmin'


class Teammoney(models.Model):
    eventid = models.IntegerField()
    spielteamid = models.IntegerField()
    tourteamid = models.IntegerField()
    moneytotal = models.IntegerField()
    moneytotal_local = models.IntegerField()
    pointtotal = models.DecimalField(max_digits=7, decimal_places=4)
    pointtotal_base = models.DecimalField(max_digits=8, decimal_places=3)
    pointtotal_two = models.DecimalField(max_digits=7, decimal_places=4)
    alternate_points = models.IntegerField()
    ppw = models.IntegerField()
    place = models.IntegerField()
    qualifier = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teammoney'


class Teamsuper(models.Model):
    superteamid = models.IntegerField(primary_key=True)
    teamname = models.CharField(max_length=50)
    siteurl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'teamsuper'


class Teamsuperlink(models.Model):
    superteamid = models.IntegerField()
    teamid = models.IntegerField()
    eventyear = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teamsuperlink'


class Teamsupernews(models.Model):
    superteamid = models.IntegerField()
    storyid = models.IntegerField()
    featured = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teamsupernews'


class Teamweb(models.Model):
    profileid = models.IntegerField()
    branchid = models.IntegerField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'teamweb'


class TeamwebSubhead(models.Model):
    profileid = models.IntegerField()
    title = models.IntegerField()
    location = models.IntegerField()
    menu = models.IntegerField()
    section_title = models.IntegerField()
    sponsordesc = models.IntegerField()
    content_width = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teamweb_subhead'


class Template(models.Model):
    templateid = models.SmallAutoField(primary_key=True)
    templatesetid = models.SmallIntegerField()
    title = models.CharField(max_length=100)
    template = models.TextField()

    class Meta:
        managed = False
        db_table = 'template'


class Templateset(models.Model):
    templatesetid = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'templateset'


class Thread(models.Model):
    threadid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    lastpost = models.PositiveIntegerField()
    forumid = models.PositiveSmallIntegerField()
    pollid = models.PositiveIntegerField()
    open = models.IntegerField()
    replycount = models.PositiveIntegerField()
    postusername = models.CharField(max_length=50)
    postuserid = models.PositiveIntegerField()
    lastposter = models.CharField(max_length=50)
    dateline = models.PositiveIntegerField()
    views = models.PositiveIntegerField()
    iconid = models.PositiveSmallIntegerField()
    notes = models.CharField(max_length=250)
    visible = models.SmallIntegerField()
    sticky = models.SmallIntegerField()
    votenum = models.PositiveSmallIntegerField()
    votetotal = models.PositiveSmallIntegerField()
    attach = models.PositiveSmallIntegerField()
    clubid = models.IntegerField()
    eventid = models.IntegerField()
    gameid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'thread'


class Threadrate(models.Model):
    threadrateid = models.AutoField(primary_key=True)
    threadid = models.PositiveIntegerField()
    userid = models.PositiveIntegerField()
    vote = models.SmallIntegerField()
    ipaddress = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'threadrate'


class Timezone(models.Model):
    timezoneid = models.IntegerField(primary_key=True)
    timezone = models.CharField(max_length=25)
    short = models.CharField(max_length=5)
    offset = models.DecimalField(max_digits=10, decimal_places=1)
    locations = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'timezone'


class Tipofweek(models.Model):
    tipid = models.AutoField(primary_key=True)
    date = models.DateField()
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    description = models.CharField(max_length=255)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipofweek'








class Tournamentflight(models.Model):
    flightid = models.AutoField(primary_key=True)
    tournamentid = models.IntegerField()
    flightname = models.CharField(max_length=50)
    sponsor = models.CharField(max_length=100)
    tier = models.IntegerField()
    priority = models.IntegerField()
    drawid_lock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentflight'


class Tournamentflightdrawteam(models.Model):
    tournamentid = models.IntegerField()
    flightid = models.IntegerField()
    drawid = models.IntegerField()
    tournamentteamid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentflightdrawteam'


class Tournamentgame(models.Model):
    tournamentid = models.ForeignKey(Tournament, models.DO_NOTHING, db_column='tournamentid')
    gameid = models.ForeignKey(Scoregame, models.DO_NOTHING, db_column='gameid')
    gamelinkid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentgame'


class Tournamentgametype(models.Model):
    gametypeid = models.IntegerField()
    gametype = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'tournamentgametype'


class Tournamentguard(models.Model):
    freeguardid = models.IntegerField(primary_key=True)
    freeguard = models.TextField()
    default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentguard'


class Tournamentlocation(models.Model):
    locationid = models.IntegerField(primary_key=True)
    tournamentid = models.IntegerField()
    locationname = models.CharField(max_length=25)
    sheetid = models.IntegerField()
    stadium_streaming = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentlocation'


class Tournamentpoints(models.Model):
    tournamentid = models.IntegerField()
    flightid = models.IntegerField()
    winpoints = models.IntegerField()
    losspoints = models.IntegerField()
    eewinpoints = models.IntegerField()
    eelosspoints = models.IntegerField()
    tiepoints = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentpoints'


class Tournamentrecord(models.Model):
    tournamentteamid = models.IntegerField()
    tournamentid = models.IntegerField()
    eventid = models.IntegerField()
    drawid = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    eewin = models.IntegerField()
    eeloss = models.IntegerField()
    ties = models.IntegerField()
    points = models.IntegerField()
    shootout = models.DecimalField(max_digits=9, decimal_places=2)
    scorefor = models.IntegerField()
    scorefor_hammer = models.IntegerField()
    scoreagainst = models.IntegerField()
    scoreagainst_hammer = models.IntegerField()
    endsfor = models.IntegerField()
    endsfor_hammer = models.IntegerField()
    endsagainst = models.IntegerField()
    endsagainst_hammer = models.IntegerField()
    blanks = models.IntegerField()
    blanksfor_hammer = models.IntegerField()
    foursfor = models.IntegerField()
    foursfor_hammer = models.IntegerField()
    threesfor = models.IntegerField()
    threesfor_hammer = models.IntegerField()
    twosfor = models.IntegerField()
    twosfor_hammer = models.IntegerField()
    foursagainst = models.IntegerField()
    foursagainst_hammer = models.IntegerField()
    threesagainst = models.IntegerField()
    threesagainst_hammer = models.IntegerField()
    twosagainst = models.IntegerField()
    twosagainst_hammer = models.IntegerField()
    fe_hammer_win = models.IntegerField()
    fe_hammer_loss = models.IntegerField()
    fe_steal_win = models.IntegerField()
    fe_steal_loss = models.IntegerField()
    fe_blank_hammer_win = models.IntegerField()
    fe_blank_hammer_loss = models.IntegerField()
    fe_blank_steal_win = models.IntegerField()
    fe_blank_steal_loss = models.IntegerField()
    fe_take1_hammer_win = models.IntegerField()
    fe_take1_hammer_loss = models.IntegerField()
    fe_give1_steal_win = models.IntegerField()
    fe_give1_steal_loss = models.IntegerField()
    fe_take1_steal_win = models.IntegerField()
    fe_take1_steal_loss = models.IntegerField()
    fe_give1_hammer_win = models.IntegerField()
    fe_give1_hammer_loss = models.IntegerField()
    fe_take2_hammer_win = models.IntegerField()
    fe_take2_hammer_loss = models.IntegerField()
    fe_give2_steal_win = models.IntegerField()
    fe_give2_steal_loss = models.IntegerField()
    fe_take2_steal_win = models.IntegerField()
    fe_take2_steal_loss = models.IntegerField()
    fe_give2_hammer_win = models.IntegerField()
    fe_give2_hammer_loss = models.IntegerField()
    fe_take3_hammer_win = models.IntegerField()
    fe_take3_hammer_loss = models.IntegerField()
    fe_give3_steal_win = models.IntegerField()
    fe_give3_steal_loss = models.IntegerField()
    fe_take3_steal_win = models.IntegerField()
    fe_take3_steal_loss = models.IntegerField()
    fe_give3_hammer_win = models.IntegerField()
    fe_give3_hammer_loss = models.IntegerField()
    le_tied_hammer_win = models.IntegerField()
    le_tied_hammer_loss = models.IntegerField()
    le_tied_steal_win = models.IntegerField()
    le_tied_steal_loss = models.IntegerField()
    le_down1_hammer_win = models.IntegerField()
    le_down1_hammer_loss = models.IntegerField()
    le_up1_steal_win = models.IntegerField()
    le_up1_steal_loss = models.IntegerField()
    le_down2_hammer_win = models.IntegerField()
    le_down2_hammer_loss = models.IntegerField()
    le_up2_steal_win = models.IntegerField()
    le_up2_steal_loss = models.IntegerField()
    le_down3_hammer_win = models.IntegerField()
    le_down3_hammer_loss = models.IntegerField()
    le_up3_steal_win = models.IntegerField()
    le_up3_steal_loss = models.IntegerField()
    le_up1_hammer_win = models.IntegerField()
    le_up1_hammer_loss = models.IntegerField()
    le_down1_steal_win = models.IntegerField()
    le_down1_steal_loss = models.IntegerField()
    le_up2_hammer_win = models.IntegerField()
    le_up2_hammer_loss = models.IntegerField()
    le_down2_steal_win = models.IntegerField()
    le_down2_steal_loss = models.IntegerField()
    le_up3_hammer_win = models.IntegerField()
    le_up3_hammer_loss = models.IntegerField()
    le_down3_steal_win = models.IntegerField()
    le_down3_steal_loss = models.IntegerField()
    ee_hammer_win = models.IntegerField()
    ee_hammer_loss = models.IntegerField()
    ee_steal_win = models.IntegerField()
    ee_steal_loss = models.IntegerField()
    one_point_win = models.IntegerField()
    one_point_loss = models.IntegerField()
    steal_take_win = models.IntegerField()
    steal_take_loss = models.IntegerField()
    steal_give_win = models.IntegerField()
    steal_give_loss = models.IntegerField()
    steal_no_take_win = models.IntegerField()
    steal_no_take_loss = models.IntegerField()
    steal_no_give_win = models.IntegerField()
    steal_no_give_loss = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentrecord'


class Tournamentrecord2(models.Model):
    tournamentteamid = models.IntegerField()
    tournamentid = models.IntegerField()
    eventid = models.IntegerField()
    drawid = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    points = models.IntegerField()
    scorefor = models.IntegerField()
    scoreagainst = models.IntegerField()
    endsfor = models.IntegerField()
    endsagainst = models.IntegerField()
    blanksfor = models.IntegerField()
    blanksfor_hammer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentrecord2'


class Tournamentrecord3(models.Model):
    tournamentteamid = models.IntegerField()
    tournamentid = models.IntegerField()
    eventid = models.IntegerField()
    drawid = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    shootout = models.DecimalField(max_digits=9, decimal_places=2)
    scorefor = models.IntegerField(blank=True, null=True)
    scoreagainst = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tournamentrecord3'


class Tournamentrecord4(models.Model):
    tournamentteamid = models.IntegerField()
    tournamentid = models.IntegerField()
    eventid = models.IntegerField()
    drawid = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    points = models.IntegerField()
    skinsfor = models.IntegerField()
    skinsfor_hammer = models.IntegerField()
    skinsagainst = models.IntegerField()
    skinsagainst_hammer = models.IntegerField()
    moneyfor = models.IntegerField()
    moneyfor_hammer = models.IntegerField()
    moneyagainst = models.IntegerField()
    moneyagainst_hammer = models.IntegerField()
    blanks = models.IntegerField()
    blanksfor_hammer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentrecord4'


class Tournamentrecordmore(models.Model):
    tournamentteamid = models.IntegerField()
    tournamentid = models.IntegerField()
    eventid = models.IntegerField()
    number_1ends = models.IntegerField(db_column='1ends')  # Field renamed because it wasn't a valid Python identifier.
    number_1ptsfor = models.IntegerField(db_column='1ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_2ends = models.IntegerField(db_column='2ends')  # Field renamed because it wasn't a valid Python identifier.
    number_2ptsfor = models.IntegerField(db_column='2ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_3ends = models.IntegerField(db_column='3ends')  # Field renamed because it wasn't a valid Python identifier.
    number_3ptsfor = models.IntegerField(db_column='3ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_4ends = models.IntegerField(db_column='4ends')  # Field renamed because it wasn't a valid Python identifier.
    number_4ptsfor = models.IntegerField(db_column='4ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_5ends = models.IntegerField(db_column='5ends')  # Field renamed because it wasn't a valid Python identifier.
    number_5ptsfor = models.IntegerField(db_column='5ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_6ends = models.IntegerField(db_column='6ends')  # Field renamed because it wasn't a valid Python identifier.
    number_6ptsfor = models.IntegerField(db_column='6ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_7ends = models.IntegerField(db_column='7ends')  # Field renamed because it wasn't a valid Python identifier.
    number_7ptsfor = models.IntegerField(db_column='7ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_8ends = models.IntegerField(db_column='8ends')  # Field renamed because it wasn't a valid Python identifier.
    number_8ptsfor = models.IntegerField(db_column='8ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_9ends = models.IntegerField(db_column='9ends')  # Field renamed because it wasn't a valid Python identifier.
    number_9ptsfor = models.IntegerField(db_column='9ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_10ends = models.IntegerField(db_column='10ends')  # Field renamed because it wasn't a valid Python identifier.
    number_10ptsfor = models.IntegerField(db_column='10ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_11ends = models.IntegerField(db_column='11ends')  # Field renamed because it wasn't a valid Python identifier.
    number_11ptsfor = models.IntegerField(db_column='11ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_12ends = models.IntegerField(db_column='12ends')  # Field renamed because it wasn't a valid Python identifier.
    number_12ptsfor = models.IntegerField(db_column='12ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_13ends = models.IntegerField(db_column='13ends')  # Field renamed because it wasn't a valid Python identifier.
    number_13ptsfor = models.IntegerField(db_column='13ptsfor')  # Field renamed because it wasn't a valid Python identifier.
    number_1ends_hammer = models.IntegerField(db_column='1ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_1ptsfor_hammer = models.IntegerField(db_column='1ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_2ends_hammer = models.IntegerField(db_column='2ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_2ptsfor_hammer = models.IntegerField(db_column='2ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_3ends_hammer = models.IntegerField(db_column='3ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_3ptsfor_hammer = models.IntegerField(db_column='3ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_4ends_hammer = models.IntegerField(db_column='4ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_4ptsfor_hammer = models.IntegerField(db_column='4ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_5ends_hammer = models.IntegerField(db_column='5ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_5ptsfor_hammer = models.IntegerField(db_column='5ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_6ends_hammer = models.IntegerField(db_column='6ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_6ptsfor_hammer = models.IntegerField(db_column='6ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_7ends_hammer = models.IntegerField(db_column='7ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_7ptsfor_hammer = models.IntegerField(db_column='7ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_8ends_hammer = models.IntegerField(db_column='8ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_8ptsfor_hammer = models.IntegerField(db_column='8ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_9ends_hammer = models.IntegerField(db_column='9ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_9ptsfor_hammer = models.IntegerField(db_column='9ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_10ends_hammer = models.IntegerField(db_column='10ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_10ptsfor_hammer = models.IntegerField(db_column='10ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_11ends_hammer = models.IntegerField(db_column='11ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_11ptsfor_hammer = models.IntegerField(db_column='11ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_12ends_hammer = models.IntegerField(db_column='12ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_12ptsfor_hammer = models.IntegerField(db_column='12ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_13ends_hammer = models.IntegerField(db_column='13ends_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_13ptsfor_hammer = models.IntegerField(db_column='13ptsfor_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_1ptsagainst = models.IntegerField(db_column='1ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_2ptsagainst = models.IntegerField(db_column='2ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_3ptsagainst = models.IntegerField(db_column='3ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_4ptsagainst = models.IntegerField(db_column='4ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_5ptsagainst = models.IntegerField(db_column='5ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_6ptsagainst = models.IntegerField(db_column='6ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_7ptsagainst = models.IntegerField(db_column='7ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_8ptsagainst = models.IntegerField(db_column='8ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_9ptsagainst = models.IntegerField(db_column='9ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_10ptsagainst = models.IntegerField(db_column='10ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_11ptsagainst = models.IntegerField(db_column='11ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_12ptsagainst = models.IntegerField(db_column='12ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_13ptsagainst = models.IntegerField(db_column='13ptsagainst')  # Field renamed because it wasn't a valid Python identifier.
    number_1ptsagainst_hammer = models.IntegerField(db_column='1ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_2ptsagainst_hammer = models.IntegerField(db_column='2ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_3ptsagainst_hammer = models.IntegerField(db_column='3ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_4ptsagainst_hammer = models.IntegerField(db_column='4ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_5ptsagainst_hammer = models.IntegerField(db_column='5ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_6ptsagainst_hammer = models.IntegerField(db_column='6ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_7ptsagainst_hammer = models.IntegerField(db_column='7ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_8ptsagainst_hammer = models.IntegerField(db_column='8ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_9ptsagainst_hammer = models.IntegerField(db_column='9ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_10ptsagainst_hammer = models.IntegerField(db_column='10ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_11ptsagainst_hammer = models.IntegerField(db_column='11ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_12ptsagainst_hammer = models.IntegerField(db_column='12ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.
    number_13ptsagainst_hammer = models.IntegerField(db_column='13ptsagainst_hammer')  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tournamentrecordmore'


class Tournamentteam(models.Model):
    tournamentteamid = models.IntegerField(primary_key=True)
    tournamentid = models.IntegerField()
    teamid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamentteam'


class Tournamenttiebreaker(models.Model):
    tournamentid = models.IntegerField()
    reason = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tournamenttiebreaker'


class TournamenttypeEvent(models.Model):
    tournamenttypeid = models.IntegerField()
    draw = models.CharField(max_length=3)
    drawname = models.CharField(max_length=100)
    startgame = models.IntegerField()
    endgame = models.IntegerField()
    restartgame = models.IntegerField()
    reendgame = models.IntegerField()
    templatename = models.CharField(max_length=100)
    qualifiers = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tournamenttype_event'


class TwitterUser(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    slug = models.CharField(max_length=10)
    consumerkey = models.CharField(db_column='consumerKey', max_length=100)  # Field name made lowercase.
    consumersecret = models.CharField(db_column='consumerSecret', max_length=100)  # Field name made lowercase.
    oauthtoken = models.CharField(db_column='oAuthToken', max_length=100)  # Field name made lowercase.
    oauthsecret = models.CharField(db_column='oAuthSecret', max_length=100)  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'twitter_user'


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    usergroupid = models.PositiveSmallIntegerField()
    talkid = models.IntegerField(db_column='talkID')  # Field name made lowercase.
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    styleid = models.PositiveSmallIntegerField()
    parentemail = models.CharField(max_length=50)
    coppauser = models.SmallIntegerField()
    homepage = models.CharField(max_length=100)
    icq = models.CharField(max_length=20)
    signature = models.TextField()
    adminemail = models.SmallIntegerField()
    showemail = models.SmallIntegerField()
    invisible = models.SmallIntegerField()
    usertitle = models.CharField(max_length=250)
    customtitle = models.SmallIntegerField()
    joindate = models.PositiveIntegerField()
    cookieuser = models.SmallIntegerField()
    daysprune = models.SmallIntegerField()
    lastvisit = models.PositiveIntegerField()
    lastactivity = models.PositiveIntegerField()
    lastpost = models.PositiveIntegerField()
    posts = models.PositiveSmallIntegerField()
    timezoneid = models.IntegerField()
    timezoneoffset = models.CharField(max_length=4)
    emailnotification = models.SmallIntegerField()
    buddylist = models.TextField()
    ignorelist = models.TextField()
    pmfolders = models.TextField()
    receivepm = models.SmallIntegerField()
    emailonpm = models.SmallIntegerField()
    pmpopup = models.SmallIntegerField()
    avatarid = models.SmallIntegerField()
    options = models.SmallIntegerField()
    birthday = models.DateField()
    maxposts = models.SmallIntegerField()
    startofweek = models.SmallIntegerField()
    ipaddress = models.CharField(max_length=20)
    referrerid = models.PositiveIntegerField()
    nosessionhash = models.SmallIntegerField()
    inforum = models.PositiveSmallIntegerField()
    clubid = models.IntegerField()
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=75)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=75)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=15)
    phonehome = models.CharField(max_length=20)
    phonework = models.CharField(max_length=20)
    phonecell = models.CharField(max_length=20)
    phoneclub = models.CharField(max_length=25)
    faxhome = models.CharField(max_length=20)
    faxwork = models.CharField(max_length=15)
    journal = models.SmallIntegerField()
    donate = models.IntegerField()
    show_donate = models.IntegerField()
    chatbox = models.IntegerField()
    fantasy_subscribe = models.IntegerField()
    reset = models.IntegerField()
    verifier = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'user'


class UserIpcheck(models.Model):
    ipid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    ipaddress = models.CharField(max_length=20)
    pin = models.IntegerField()
    date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_ipcheck'


class UserPasswordBase(models.Model):
    baseid = models.AutoField(primary_key=True)
    base = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'user_password_base'


class UserPasswordLink(models.Model):
    userid = models.IntegerField()
    baseid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_password_link'


class Useractivation(models.Model):
    useractivationid = models.AutoField(primary_key=True)
    userid = models.PositiveIntegerField()
    dateline = models.PositiveIntegerField()
    activationid = models.CharField(max_length=20)
    type = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'useractivation'


class Userfield(models.Model):
    userid = models.PositiveIntegerField(primary_key=True)
    field2 = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'userfield'


class Usergroup(models.Model):
    usergroupid = models.SmallAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    usertitle = models.CharField(max_length=100)
    cancontrolpanel = models.SmallIntegerField()
    canmodifyprofile = models.SmallIntegerField()
    canviewmembers = models.SmallIntegerField()
    canview = models.SmallIntegerField()
    cansearch = models.SmallIntegerField()
    canemail = models.SmallIntegerField()
    canpostnew = models.SmallIntegerField()
    canmove = models.SmallIntegerField()
    canopenclose = models.SmallIntegerField()
    candeletethread = models.SmallIntegerField()
    canreplyown = models.SmallIntegerField()
    canreplyothers = models.SmallIntegerField()
    canviewothers = models.SmallIntegerField()
    caneditpost = models.SmallIntegerField()
    candeletepost = models.SmallIntegerField()
    canusepm = models.SmallIntegerField()
    canpostpoll = models.SmallIntegerField()
    canvote = models.SmallIntegerField()
    canpostattachment = models.SmallIntegerField()
    canpublicevent = models.SmallIntegerField()
    canpublicedit = models.SmallIntegerField()
    canthreadrate = models.SmallIntegerField()
    maxbuddypm = models.PositiveSmallIntegerField()
    maxforwardpm = models.PositiveSmallIntegerField()
    cantrackpm = models.SmallIntegerField()
    candenypmreceipts = models.SmallIntegerField()
    canwhosonline = models.SmallIntegerField()
    canwhosonlineip = models.SmallIntegerField()
    ismoderator = models.SmallIntegerField()
    showgroup = models.PositiveSmallIntegerField()
    cangetattachment = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'usergroup'


class Userinfo(models.Model):
    userinfoid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postalcode = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    generalnews = models.IntegerField()
    format = models.IntegerField()
    tipnews = models.IntegerField()
    clubnews = models.IntegerField()
    octnews = models.IntegerField()
    wctnews = models.IntegerField()
    morrisnews = models.IntegerField()
    clubid = models.IntegerField()
    emailsent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userinfo'


class Usernewsletter(models.Model):
    userid = models.IntegerField(primary_key=True)
    generalnews = models.IntegerField()
    tipnews = models.IntegerField()
    clubnews = models.IntegerField()
    octnews = models.IntegerField()
    wctnews = models.IntegerField()
    morrisnews = models.IntegerField()
    format = models.IntegerField()
    emailsent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usernewsletter'


class UsersUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Usertitle(models.Model):
    usertitleid = models.SmallAutoField(primary_key=True)
    minposts = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'usertitle'


class VbLinks(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    banner = models.CharField(max_length=255)
    banner_url = models.CharField(max_length=255)
    banner_text = models.CharField(max_length=255)
    description = models.TextField()
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=255)
    supporter = models.IntegerField()
    forumlink = models.CharField(max_length=255)
    counter = models.IntegerField()
    joindate = models.IntegerField()
    lastedit = models.IntegerField()
    online = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vb_links'


class VbLinksCategory(models.Model):
    name = models.CharField(max_length=255)
    sortorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vb_links_category'


class Venue(models.Model):
    venueid = models.AutoField(primary_key=True)
    venuename = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=75)
    province = models.IntegerField()
    country = models.IntegerField()
    postal = models.CharField(max_length=12)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=155)

    class Meta:
        managed = False
        db_table = 'venue'


class Videos(models.Model):
    videoid = models.AutoField(primary_key=True)
    videotypeid = models.IntegerField()
    isnews = models.IntegerField()
    eventid = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    code = models.TextField()
    user = models.CharField(max_length=50)
    channelid = models.IntegerField()
    date = models.IntegerField()
    submittedby = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videos'


class VideosCategory(models.Model):
    categoryid = models.AutoField(primary_key=True)
    videoid = models.IntegerField()
    eventtypeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videos_category'


class VideosChannel(models.Model):
    channelid = models.AutoField(primary_key=True)
    channel = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    videotypeid = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videos_channel'


class VideosGame(models.Model):
    videoid = models.IntegerField()
    gameid = models.IntegerField()
    package = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videos_game'


class VideosPlayer(models.Model):
    playerid = models.IntegerField()
    videoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videos_player'


class VideosPlaylist(models.Model):
    playlistid = models.AutoField(primary_key=True)
    playlist = models.CharField(max_length=100)
    playlistdesc = models.TextField()
    lastpost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videos_playlist'


class VideosPlaylistLink(models.Model):
    playlistid = models.IntegerField()
    videoid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videos_playlist_link'


class VideosTeam(models.Model):
    teamid = models.IntegerField()
    videoid = models.IntegerField()
    teamvideo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videos_team'


class Videotype(models.Model):
    videotypeid = models.AutoField(primary_key=True)
    videotype = models.CharField(max_length=25)
    urlcode = models.CharField(max_length=255)
    urlcode_end = models.CharField(max_length=255)
    admincode = models.CharField(max_length=255)
    admincode_end = models.CharField(max_length=255)
    embed = models.IntegerField()
    replay = models.IntegerField()
    needscode = models.IntegerField()
    searchcode = models.CharField(max_length=25)
    imgcode = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'videotype'


class VideotypeEmbed(models.Model):
    veid = models.AutoField(primary_key=True)
    videotypeid = models.IntegerField()
    embed_code = models.TextField()
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'videotype_embed'


class WatchNetwork(models.Model):
    networkid = models.AutoField(primary_key=True)
    sectionid = models.IntegerField()
    network = models.CharField(max_length=100)
    networkdesc = models.TextField()
    networklogo = models.CharField(max_length=50)
    networkurl = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'watch_network'


class WatchTeam(models.Model):
    profileid = models.IntegerField()
    streamtitle = models.CharField(max_length=100)
    streamurl = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'watch_team'


class Word(models.Model):
    wordid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'word'
