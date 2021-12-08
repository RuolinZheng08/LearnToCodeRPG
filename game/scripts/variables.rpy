init:
    default stats_unlocked = False
    default stats_knowledge_unlocked = False # cs knowledge
    default todo_unlocked = False

    # alternative endings
    default has_triggered_ending_barista = False
    default has_triggered_ending_cat = False
    default has_triggered_ending_tutor = False
    default has_triggered_ending_office = False

    default num_times_sanity_low = 0
    default has_triggered_ending_farmer = False

    default has_triggered_ending_today = False

    # set question type during study session
    default study_session_questions = general_questions

    default has_visited_hacker_space_with_annika = False

    # unlocks Marco's topics_to_ask
    default has_met_marco = False

    # major characters and plot have been introduced, unlocks alternative endings
    default has_met_layla = False

    # once this is True, trivia guy no longer appears, and player can get a first round interview w/ CupCakeCPU
    default has_won_hacker_space_trivia = False
    default has_applied_to_cupcakecpu = False

    # player_stats.player_stats_map['CS Knowledge'] >= 80
    default has_completed_curriculum = False

    default has_received_offer = False
    # TODO: beyond demo version, can do negotiation
    default has_accepted_offer = False

    default day_activity = None # set in day_activity_choice.rpy

    # interview and offer
    default interview_company_name = None # set in day_activity_choice.rpy
    default offer_company_name = None # set in quiz_session.rpy

    # seen labels
    default seen_hacker_space_events = set()
    default seen_barista_events = set()

    default persistent.enable_save_reminder = None

init python:
    if persistent.achievements is None:
        persistent.achievements = set()

    # npc Q and A
    topics_to_ask = set()
    npc = annika
    npc_sprite = 'annika'

    ## Non-mutable

    # to-do strings
    todo_check_fcc = 'Check out [freeCodeCamp]'
    todo_ask_curriculum = 'Ask Annika about CS curriculum'
    todo_learn_cs = 'Bump {b}CS Knowledge{/b} to 80+'
    todo_apply_cupcakecpu = 'Apply to CupcakeCPU'
    todo_apply_to_jobs = 'Start applying to jobs'
    todo_interview_prep = 'Start preparing for coding interviews'
    todo_get_job = 'Get a developer job'
    todo_ask_hackathon = 'Learn about Hackathon'
    todo_ask = 'Learn about ' # should be concatenated with vocabs from barista story

    day_acitivity_study = 'Study CS Fundamentals' # will later change into todo_interview_prep

    # story labels for hacker space and barista
    hacker_space_event_labels = [
    'hacker_space_tech_talk',
    'hacker_space_playtest',
    'hacker_space_project',
    'hacker_space_open_source',
    ]

    barista_event_labels = [
    'barista_fullstack',
    'barista_devops',
    'barista_conference',
    'barista_versioncontrol',
    'barista_machinelearning',
    'barista_agile',
    'barista_api',
    'barista_userexperience',    
    ]

    # map topic to label name
    ask_npc = {
    'Hackathon': 'ask_hackathon',
    'Full-Stack': 'ask_fullstack',
    'DevOps': 'ask_devops',
    'Conference': 'ask_conference',
    'Version Control': 'ask_versioncontrol',
    'Machine Learning': 'ask_machinelearning',
    'Agile': 'ask_agile',
    'API': 'ask_api',
    'User Experience': 'ask_userexperience',
    }

    # VIP names and profile links
    quincy_profile = 'https://twitter.com/ossia'
    abbey_profile = 'https://twitter.com/abbeyrenn'
    lynn_profile = 'https://ruolinzheng08.github.io/'
    vip_names = {
    'Quincy': quincy_profile, 
    'Quincy Larson': quincy_profile, 
    'Lynn': lynn_profile, 
    'Lynn Zheng': lynn_profile, 
    'Abbey': abbey_profile, 
    'Abbey Rennemeyer': abbey_profile
    }

    # tweets generated by https://tech.cymi.org/tweet-intents
    # Note to proofreader: please do click on each tweet link and proofread the tweet content
    tweet_default = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20just%20discovered%20this%20cool%20game%20called%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_hackerspace = "https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20just%20discovered%20the%20Hackerspace%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A"

    ## milestone
    milestone_complete_curriculum = 'Nailed the Curriculum'
    milestone_first_interview = 'Got My First Interview'
    milestone_first_offer = 'Got My First Offer'
    # TODO: v2 can have multiple offers
    milestone_sign_offer = 'Now Streaming: My Dream Dev Job'

    tweet_complete_curriculum = tweet_default
    tweet_first_interview = tweet_default
    tweet_first_offer = tweet_default
    tweet_sign_offer = tweet_default

    milestone_to_tweet_map = {
        milestone_complete_curriculum: tweet_complete_curriculum,
        milestone_first_interview: tweet_first_interview,
        milestone_first_offer: tweet_first_offer,
        milestone_sign_offer: tweet_sign_offer
    }

    ## plot
    plot_cookie = 'Late-night Cookie Crunch'
    plot_trivia = 'Tech Trivia Guru'
    plot_quiz_all = 'Got all quiz questions correct in a session'
    plot_quiz_none = 'Bombed all quiz questions in a session'
    # TODO: vip, barista, hackerspace, minigame, saving up all buzzwords, asking all to Marco or all to Annika
    # too chill etc.

    # TODO: none default tweet
    plot_bonus_to_tweet_map = {
        plot_cookie: tweet_default,
        plot_trivia: tweet_default,
        plot_quiz_all: tweet_default,
        plot_quiz_none: tweet_default
    }

    ## quiz
    # questions that have a `wait thats not a cs question` label
    # quiz_fcc_history
    quiz_bonus_to_tweet_map = {

    }

    ## endings
    ending_barista = 'Now serving {font=fonts/saxmono.ttf}0xc0ffee{/font}'
    ending_cat = 'Cat Who Codes'
    ending_tutor = 'Coding It Forward'
    ending_office = 'Just Another Day at the Office'
    ending_farmer = 'Nature Lover at Heart'
    ending_dev = 'Dev Who Brought Down Prod on the First Day'

    tweet_end_barista = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20ended%20up%20becoming%20a%20barista%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_cat = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20found%20my%20cat%20coding%20on%20my%20laptop%20in%20the%20middle%20of%20the%20night%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_tutor = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20ended%20up%20becoming%20a%20CS%20teacher%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_office = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20ended%20up%20becoming%20an%20office%20worker%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_farmer = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20ended%20up%20becoming%20a%20farmer%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'
    tweet_end_dev = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.freecodecamp.org%2Flearn-to-code-rpg&text=I%20taught%20myself%20to%20code%2C%20got%20a%20tech%20job%2C%20and%20brought%20down%20prod%20on%20my%20first%20day%20of%20work%20in%20%23LearnToCodeRPG.%20Play%20it%20here%3A'

    ending_to_tweet_map = {
        ending_barista: tweet_end_barista,
        ending_cat: tweet_end_cat,
        ending_tutor: tweet_end_tutor,
        ending_office: tweet_end_barista,
        ending_farmer: tweet_end_farmer,
        ending_dev: tweet_end_dev,
    }

    ## master labels and maps
    plot_achievement = 'Plot Milestones'
    plot_bonus = 'Plot Easter Eggs'
    quiz_bonus = 'Quiz Question Easter Eggs'
    ending_achievement = 'Endings'

    achievement_labels_map = {
        plot_achievement: milestone_to_tweet_map,
        plot_bonus: plot_bonus_to_tweet_map,
        quiz_bonus: quiz_bonus_to_tweet_map,
        ending_achievement: ending_to_tweet_map
    }

    # master map for easy lookup in script.rpy
    all_tweet_map = {}
    for tweet_map in [
        milestone_to_tweet_map, 
        plot_bonus_to_tweet_map, 
        quiz_bonus_to_tweet_map, 
        achievement_labels_map
    ]:
        all_tweet_map.update(tweet_map)

    ## rhythm game
    # define the song titles and their files
    rhythm_game_songs = [
        Song('Chasing That Feeling', 'audio/bgm/Chasing That Feeling.mp3', 'audio/bgm/Chasing That Feeling.beatmap.txt'),
        Song('Crystalize That Child in Me', 'audio/bgm/Crystalize That Child in Me.mp3', 'audio/bgm/Crystalize That Child in Me.beatmap.txt'),
        Song('Never Not Favored', 'audio/bgm/Never Not Favored.mp3', 'audio/bgm/Never Not Favored.beatmap.txt'),
        Song('Press Your Advantage', 'audio/bgm/Press Your Advantage.mp3', 'audio/bgm/Press Your Advantage.beatmap.txt')
    ]
    # must be persistent to be able to record the scores
    if persistent.rhythm_game_high_scores is None:
        persistent.rhythm_game_high_scores = {
        song.name: (0, 0) for song in rhythm_game_songs
    }