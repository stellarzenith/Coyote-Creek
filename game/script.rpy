
        #
        ##
        ### ---COYOTE CREEK--- ###
        ##
        #
        ## ---INDEX--- ##
        #
        # ---VARIABLES--- #
        # ---CHARACTER CREATION--- #
        # ---INTRODUCTION--- #
        # ---DAYS OF THE WEEK--- #
        # ---LOCATIONS--- #
        # ---NPC DIALOGUE--- #
        # ---ROMANTIC EVENTS--- #
        #

define player = Character("[name]")
define unknown = Character("???")
define n = Character("Norman", color="#4169e1")
define m = Character("Mike", color="#149214")
define k = Character("Kessler", color="#d00f0f")
define s = Character("Scott", color="#7b1ddf")
define l = Character("Liz")
define j = Character("Julie")
define ro = Character("Rosa")
define b = Character("Brandy")
define lo = Character("Lori")
define ma = Character("Marie")
define bi = Character("Billy")
define jo = Character("Joaquin")
define h = Character("Hastiin")
define he = Character("Chief Hernandez")
define ja = Character("Javier")
define ri = Character("Riley")
define c = Character("Coyote Craig")
define ccm = Character("The Coyote Creek Monster")
image black = "#000"


label start:
        #
        # ---VARIABLES--- #
        #
        # ---Relationship points--- #
    $ normanpoints = 0
    $ mikepoints = 0
    $ kesslerpoints = 0
    $ scottpoints = 0
    $ lizpoints = 0
    $ juliepoints = 0
    $ rosapoints = 0
    $ brandypoints = 0
    $ loripoints = 0
    $ mariepoints = 0
    $ billypoints = 0
    $ joaquinpoints = 0
    $ hernandezpoints = 0
    $ hastiinpoints = 0
    $ javierpoints = 0
    $ rileypoints = 0
        # ---Current day & location--- #
    $ currentday = "Monday"
    $ currenttime = "day"
    $ currentloc = "motelroom"
        # ---Events done--- #
    $ monevent = "none"
    $ tueevent = "none"
    $ wedevent = "none"
    $ thuevent = "none"
    $ frievent = "none"
    $ satevent = "none"
        # ---NPC Locations--- #
    $ normanloc = "diner"
    $ mikeloc = "garagefront"
    $ kesslerloc = "motelfront"
    $ scottloc = "giftstore"
    $ lizloc = "motellobby"
    $ julieloc = "none"
    $ rosaloc = "none"
    $ brandyloc = "none"
    $ loriloc = "none"
    $ marieloc = "none"
    $ billyloc = "none"
    $ joaquinloc = "none"
    $ hernandezloc = "none"
    $ hastiinloc = "none"
    $ javierloc = "none"
    $ rileyloc = "none"
        # ---Has a character been talked to today?--- #
    $ normantalkedto = 0
    $ miketalkedto = 0
    $ kesslertalkedto = 0
    $ scotttalkedto = 0
    $ liztalkedto = 0
    $ julietalkedto = 0
    $ rosatalkedto = 0
    $ brandytalkedto = 0
    $ loritalkedto = 0
    $ marietalkedto = 0
    $ billytalkedto = 0
    $ joaquintalkedto = 0
    $ hernandeztalkedto = 0
    $ hastiintalkedto = 0
    $ javiertalkedto = 0
    $ rileytalkedto = 0
        # ---Unlocked Locations--- #
    $ mainstreet = False
    $ highschool = False
    $ forest = False
    $ farm = False
    $ ridge = False
        # ---Array of every talked to status. Resets every day--- #
    $ talkedto = [normantalkedto, miketalkedto, kesslertalkedto, scotttalkedto, liztalkedto, julietalkedto, rosatalkedto, brandytalkedto, loritalkedto, marietalkedto, billytalkedto, joaquintalkedto, hernandeztalkedto, hastiintalkedto, javiertalkedto, rileytalkedto]

        #
        # ---CHARACTER CREATION--- #
        #
    scene black
    label nameselect:
        python:
            name = renpy.input("What is your first name?", default="Frankie")
            name = name.strip()
            if not name:
                name = "Frankie"
            surname = renpy.input("What is your last name?", default="Williams")
            surname = surname.strip()
            if not surname:
                surname = "Williams"
        menu:
            "Is [name] [surname] correct?"
            "Yes":
                jump introduction
            "No":
                jump nameselect
        #
        # ---INTRODUCTION--- #
        #
    label introduction:
        pause 3
        "We broke down a few miles outside of a small, backwater town in northern Arizona. I was asleep when it happened."
        "We had to push the damn thing all the way into town. It was hot, dusty, and way too bright for someone who had just woken up in the back of an RV."
        "Norman, my best friend, took it in stride, as he does with most things. To him, a breakdown is just another adventure on the road trip. He’s always had that optimism."
        "His chipper demeanor faded into one of confusion once he popped the hood and immediately saw why the van was no longer running."
        "The entire thing was overgrown with plant life."
        scene bg garagefront day
        with fade
        "Now the van sits outside the local garage, with myself and Norman slumped against it in the dust. We both gasp for breath and pass a bottle of water between us, drenched in sweat. The sun is high in the sky and beating down hard."
        "Norman turns to me, a smile on his face in spite of his clear exhaustion, and breathes in relief."
        show norman
        with dissolve
        n "\"Are you as hungry as I am right now?\""
        "I am pretty hungry, I notice. I had been too busy pushing the van to realise until now."
        player "\"Yeah, actually. We didn’t get a chance to grab breakfast.\""
        "Norman scans the street slowly, frowning."
        n "\"I’ll see if I can find somewhere we can get some food.\""
        "He furrows his brow and glances toward the van."
        n "\"I don't understand anything about what happened... The engine was perfect.\""
        "He shakes the worry from his face and gives me a small smile, his eyes sparkling."
        n "\"How about you see the mechanic about it? I'll find us some food.\""
        "Before disappearing, he waves over his shoulder and shouts."
        n "\"I’ll try to find a local map too!\""
        hide norman
        with dissolve
        "With that, he’s gone, and I’m left alone."
        scene bg garage day
        with fade
        "The air inside the garage is thick with the smell of oil. It’s almost hard to breathe."
        "I hear music from a cassette player on one of the many shelves that line the walls. The only other noise is that of the mechanic himself at work underneath a jacked up car."
        "All I can see of him are his legs, and occasionally his hand reaching for a new tool. He hums to the chorus of the song playing."
        "He pushes himself out from underneath the car and sits up to wipe his forehead, still tapping his foot to the music. He notices me standing there, and stands to greet me with a smile on his face."
        show mike
        with dissolve
        "His hair is short, messy and slick with motor oil. From the various patches sewn clumsily onto his jumpsuit, it’s clear that he’s a fan of science fiction."
        "He cleans off his glasses and leans against the car, still smiling at me."
        m "\"Hey, I’m Mike. How can I help you?\""
        player "\"My friend and I actually had our van break down outside of town…\""
        "I hesitate. How do I even explain something like this?"
        player "\"We have a... uh... Strange problem.\""
        "Mike chuckles and gestures to the door behind me."
        m "\"Alright? Let's go see what the problem is.\""
        hide mike
        with dissolve
        scene bg garagefront day
        with fade
        "Mike follows me out to the van, whistling the tune from his cassette player."
        show mike
        with dissolve
        m "\"Let's see your strange problem then.\""
        "I open the driver-side door and pop the hood."
        m "\"... Um.\""
        "He stares at the overgrown engine in bewilderment, unable to comprehend what he sees."
        "No longer disoriented from the grogginess of just waking up, I take my own first good look at it."
        m "\"... What am I looking at here?\""
        player "\"Uhh... I have no idea. It just appeared.\""
        m "\"That... Huh. Okay?\""
        m "\"I guess I can see how bad the damage is and remove as much as I can. This isn't going to be a quick job though.\""
        player "\"Yeah, I figured...\""
        "Mike closes the hood and flashes me a smile."
        m "\"Well. I'll try to clear this out. I reckon it'll take a few days... But I'll try.\""
        m "\"There's a motel right across the street if you're looking for a place to stay. The owners are good friends of mine.\""
        player "\"I guess I'll go check it out. Thanks Mike.\""
        hide mike
        with dissolve
        scene bg motel day
        with fade
        "The motel lobby is way too brightly lit. The decorating in here is tacky, and it’s clear they don’t get a lot of business."
        "Behind the front desk sits a woman with light hair and green eyes who doesn’t look like she wants to be there at all."
        "She’s flipping through a magazine absentmindedly. I don’t think she’s even noticed I’m here yet."
        show liz
        with dissolve
        unknown "\"... Can I help you?\""
        "Yes she has."
        player "\"Uh. I'm looking for a room.\""
        "The woman closes her magazine and tosses it onto the counter in front of her. She opens a drawer and rummages in it for a second before pulling out a ledger and opening it, turning it to face me."
        unknown "\"Rates are listed here. Sign and I'll get you a key.\""
        "I get a room with two beds. The woman hands me a key and picks up her magazine again."
        l "\"Thanks. I'm Liz, by the way. If you need anything I'm usually here. If not, my brother runs the gift store next door.\""
        hide liz
        with dissolve
        window show
        scene bg motel day
        with hpunch
        window auto
        "When I turn to check out said gift store, I find myself bumping into someone on their way in."
        show daniel
        with dissolve
        unknown "\"‘scuse me.\""
        "The man in front of me has dark, curly hair and a scratchy shadow of stubble on his face."
        "He looks at me with tired eyes and nurses the coffee cup in his hand."
        unknown "\"You don't look local. Me neither.\""
        k "\"Kessler. Private Investigator. Mayor called me in.\""
        k "\"Town's got some kind of vandalism problem, from what I hear.\""
        "That’s when I notice a small face peek out from behind him."
        show julie
        with dissolve
        "Trailing along behind the man is a young girl who peers up at me cautiously, clutching firmly onto him. Kessler glances down at her and sighs, ruffling her hair."
        "She tugs on the leg of his pants urgently, a sign of discomfort."
        k "\"I better get moving. Got some work to do.\""
        "He grumbles to himself and moves past me, into the parking lot."
        k "\"Be seeing you.\""
        hide daniel
        with dissolve
        hide julie
        with dissolve
        "With that, I’m left in the motel lobby with Liz again, who has evidently not been paying attention to our exchange and doesn’t seem to care."
        scene bg giftstore day
        with fade
        "The souvenirs that line the shelves look like they've been here for months. There's a layer of dust coating each one."
        "Behind the desk sits a man who has fallen asleep in his wheelchair. Like the main section of the motel, this gift shore doesn't seem to get much business."
        "I clear my throat and make my presence known. The man jolts awake and his eyes light up at the sight of a potential customer."
        show scott
        with dissolve
        "His relation to Liz is evident in his face. He has the same light hair and green eyes, though he looks considerably less stern and more uncertain."
        s "\"Welcome to Cooper's Motel & Gift Store! I'm Scott, what can I do for you?\""
        player "\"Just looking... I'm [name]. I'm new in town and thought I'd introduce myself.\""
        "He looks a bit let down, but quickly regains his cheery composure."
        s "\"Pleasure to meet you! It's rare to see fresh faces in Coyote Creek... It's a shame, really. This town has a lot of charm.\""
        "He glances back at the objects on display and frowns."
        s "\"... It really is an underrated place.\""
        "He snaps out of it and looks back at me, his smile returning to his face."
        s "\"I hope you like it here. Feel free to drop by whenever you want. I've always got time.\""
        hide scott
        with dissolve
        scene black
        "Norm's van is, for lack of a better term, completely fucked."
        "... It looks like we'll be sticking around here for at least a week while it gets fixed."
        "I have my doubts that anything of note will happen while we're here, but..."
        "... Maybe I'll find myself surprised."
        $ persistent.seenintro = True
        #
        # ---DAYS OF THE WEEK--- #
        #
        # ---MONDAY--- #
        #
    label monday:
        scene black
        pause 1
        show text "{color=#fff}Monday, June 23rd, 1986{/color}" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        pause 3
        "..."
        n "\"Hey, wake up.\""
        n "\"Come on, [name], I'm hungry. Let's go!\""
        scene bg motelroom day
        with fade
        show norman
        with dissolve
        player "\"Ugh... What time is it?\""
        n "\"Eight. The diner's doing a breakfast special, come on.\""
        "I close my eyes again. Norman immediately groans."
        n "\"Y'know what? Alright. I'll be there. Get up whenever you're ready.\""
        hide norman
        with dissolve
        "Before I have a chance to reply, he hurries out of the room and closes the door behind him."
        scene black
    label move:
        call screen movement() with fade
        #
        # ---TUESDAY--- #
        #
    label tuesday:
        $ talkedto[talkedto>0]=0
        $ currentday = "Tuesday"
        scene black
        pause 1
        show text "{color=#fff}Tuesday, June 24th, 1986{/color}" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        pause 3
        #
        # ---WEDNESDAY--- #
        #
    label wednesday:
        $ talkedto[talkedto>0]=0
        $ currentday = "Wednesday"
        scene black
        pause 1
        show text "{color=#fff}Wednesday, June 25th, 1986{/color}" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        pause 3
        #
        # ---THURSDAY--- #
        #
    label thursday:
        $ talkedto[talkedto>0]=0
        $ currentday = "Thursday"
        scene black
        pause 1
        show text "{color=#fff}Thursday, June 26th, 1986{/color}" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        pause 3
        #
        # ---FRIDAY--- #
        #
    label friday:
        $ talkedto[talkedto>0]=0
        $ currentday = "Friday"
        scene black
        pause 1
        show text "{color=#fff}Friday, June 27th, 1986{/color}" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        pause 3
        #
        # ---SATURDAY--- #
        #
    label saturday:
        $ talkedto[talkedto>0]=0
        $ currentday = "Saturday"
        scene black
        pause 1
        show text "{color=#fff}Saturday, June 28th, 1986{/color}" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        pause 3
        #
        # ---SUNDAY--- #
        #
    label sunday:
        $ currentday = "Sunday"
        scene black
        pause 1
        show text "{color=#fff}Sunday, June 29th, 1986{/color}" at truecenter
        with dissolve
        pause 5
        hide text
        with dissolve
        pause 3
        "... It's time to go home."
        scene bg motelroom day
        with fade
        "It looks like Norman's already gotten up."
        "I guess I should say goodbye to people before we get in the van."
        if normanpoints >= 5:
            "... At least I wont be saying goodbye to Norman."
        elif mikepoints >= 5:
            "... I'm really gonna miss Mike."
        elif kesslerpoints >= 5:
            "... I'm really gonna miss Daniel."
        elif scottpoints >= 5:
            "... I'm really gonna miss Scott."
        #
        # ---NORMAN'S ENDING--- #
        #
        if normanpoints >= 5:
            "You got Norman's best end."
        elif normanpoints >= 2:
            "You got Norman's good end."
        elif normanpoints >= -1:
            "You got Norman's neutral end."
        elif normanpoints >= -4:
            "You got Norman's bad end."
        else:
            "You got Norman's worst end."
        #
        # ---MIKE'S ENDING--- #
        #
        if mikepoints >= 5:
            "You got Mike's best end."
        elif mikepoints >= 2:
            "You got Mike's good end."
        elif mikepoints >= -1:
            "You got Mike's neutral end."
        elif mikepoints >= -4:
            "You got Mike's bad end."
        else:
            "You got Mike's worst end."
        #
        # ---KESSLER'S ENDING--- #
        #
        if kesslerpoints >= 5:
            "You got Kessler's best end."
        elif kesslerpoints >= 2:
            "You got Kessler's good end."
        elif kesslerpoints >= -1:
            "You got Kessler's neutral end."
        elif kesslerpoints >= -4:
            "You got Kessler's bad end."
        else:
            "You got Kessler's worst end."
        #
        # ---SCOTT'S ENDING--- #
        #
        if scottpoints >= 5:
            "You got Scott's best end."
        elif scottpoints >= 2:
            "You got Scott's good end."
        elif scottpoints >= -1:
            "You got Scott's neutral end."
        elif scottpoints >= -4:
            "You got Scott's bad end."
        else:
            "You got Scott's worst end."
        return
        #
        # ---LOCATIONS--- #
        #
        #
        # ---NPC DIALOGUE--- #
        #
label npcdialogue:
        #
        # ---NORMAN--- #
        #
    label normandialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday" and currenttime == "day":
            menu:
                n "\"Something you need, [name]?\""
                "Talk" if normantalkedto == 0:
                    "Norman tilts his head in greeting."
                    n "\"Finally out of bed?\""
                    player "\"Mmhm… You seemed excited about this place.\""
                    n "\"What can I say? I like trying new food.\""
                    player "\"Does it bother you that we're stuck here?\""
                    n "\"Nah. It's just a bump in the road, right?\""
                    menu:
                        n "\"What happened with the van is weird, but… I’m not worried.\""
                        "\"That doesn't seem smart.\"":
                            $ normanpoints -= 0.5
                            "He frowns at me."
                            n "\"Maybe not, but...\""
                        "\"Hopefully the mechanic can fix it.\"":
                            $ normanpoints += 0.5
                            "He cracks a smile and shrugs."
                            n "\"In the meantime, let’s have some fun while we’re here.\""
                    $ normantalkedto = 1
                    jump normandialogue
                "Spend today with Norman" if normantalkedto == 1:
                    menu:
                        n "\"So, you hungry?\""
                        "\"Starving.\"":
                            n "\"Sit down then!\""
                            $ monevent = "Norman"
                            jump normanmon
                        "\"Actually, let me get back to you.\"":
                            n "\"Alright! I'll be here.\""
                    jump normandialogue
                "Leave":
                    n "\"Later then!\""
                    return
        elif currenttime == "night":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
             menu:
                "Talk" if normantalkedto == 0:
                    $ normantalkedto = 1
                    jump normandialogue
                "Spend today with Norman" if normantalkedto == 1:
                    menu:
                        " ":
                            jump normantue
                        " ":
                            return
                    jump normandialogue
                "Leave":
                    return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            menu:
                "Talk" if normantalkedto == 0:
                    $ normantalkedto = 1
                    jump normandialogue
                "Spend today with Norman" if normantalkedto == 1:
                    menu:
                        " ":
                            jump normanwed
                        " ":
                            return
                    jump normandialogue
                "Leave":
                    return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            menu:
                "Talk" if normantalkedto == 0:
                    $ normantalkedto = 1
                    jump normandialogue
                "Spend today with Norman" if normantalkedto == 1:
                    menu:
                        " ":
                            jump normanthu
                        " ":
                            return
                    jump normandialogue
                "Leave":
                    return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            menu:
                "Talk" if normantalkedto == 0:
                    $ normantalkedto = 1
                    jump normandialogue
                "Spend today with Norman" if normantalkedto == 1:
                    menu:
                        " ":
                            jump normanfri
                        " ":
                            return
                    jump normandialogue
                "Leave":
                    return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            menu:
                "Talk" if normantalkedto == 0:
                    $ normantalkedto = 1
                    jump normandialogue
                "Spend today with Norman" if normantalkedto == 1:
                    menu:
                        " ":
                            jump normansat
                        " ":
                            return
                    jump normandialogue
                "Leave":
                    return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---MIKE--- #
        #
    label mikedialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            menu:
                m "\"You got a minute, [name]?\""
                "Talk" if miketalkedto == 0:
                    m "\"This engine has me completely stumped. I've never seen anything like it.\""
                    player "\"Any idea what caused it?\""
                    menu:
                        m "\"Well... Nothing that doesn't involve aliens.\""
                        "\"Oh. Great.\"":
                            $ mikepoints -= 0.5
                            "He looks embarrassed."
                        "\"Oh, great!\"":
                            $ mikepoints += 0.5
                            "His face breaks into the widest grin I've ever seen."
                    m "\"I know it's silly, but if you're interested... I can tell you about it.\""
                    jump mikedialogue
                "Spend today with Mike" if miketalkedto == 1:
                    menu:
                        m "\"I've got some time if you want to know more about your engine trouble.\""
                        "\"Sure, I'll listen.\"":
                            m "\"Step into my office!\""
                            $ monevent = "Mike"
                            jump mikemon
                        "\"Hold on, I have things I need to do.\"":
                            m "\"No worries, [name]. I'm not going anywhere.\""
                    jump mikedialogue
                "Leave":
                    m "\"Bye!\""
                    return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---KESSLER--- #
        #
    label kesslerdialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday" and currenttime == "day":
            menu:
                k "\"[surname].\""
                "Talk" if kesslertalkedto == 0:
                    player "\"You look stressed out.\""
                    k "\"Hm. That's because I am.\""
                    player "\"Can I ask why?\""
                    k "\"Urgh... Some kid keeps vandalising property and I can't find him.\""
                    menu:
                        k "\"I was actually just about to head out looking for him.\""
                        "\"Okay. Bye.\"":
                            $ kesslerpoints -= 0.5
                            "He takes a slow sip of his coffee."
                        "\"Anything I can do to help?\"":
                            $ kesslerpoints += 0.5
                            k "\"Might be good to have the eyes of someone else who isn't local, actually.\""
                            k "\"Let me know if you see anything out of the ordinary.\""
                    $ kesslertalkedto = 1
                    jump kesslerdialogue
                "Spend today with Kessler" if kesslertalkedto == 1:
                    menu:
                        k "\"Should get going soon...\""
                        "\"I'll join you!\"":
                            k "\"... Okay? Actually. Sure. Why not.\""
                            k "\"Don't tell nobody I'm letting you come along though.\""
                            $ monevent == "Daniel"
                            jump kesslermon
                        "\"See you later.\"":
                            "Mmhm."
                    jump kesslerdialogue
                "Leave":
                    "Kessler nods."
                    return
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---SCOTT--- #
        #
    label scottdialogue:
        scene bg [currentloc] [currenttime]
        show scott
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            menu:
                s "\"Hey, Mr. [surname], welcome!\""
                "Talk" if scotttalkedto == 0:
                    $ scotttalkedto = 1
                    "Scott's bright eyes watch me hopefully."
                    s "So... Anything I can do for you?"
                    "My eyes immediately jump to the tacky model skeleton, propped up on the counter. Its skull is adorned with a gaudy cowboy hat."
                    "Scott seems to notice my interest and speaks up."
                    s "That right there is Buffalo Bones."
                    "He says it with full confidence, as if that alone should explain everything."
                    player "... Huh?"
                    "There's a moment of silence before he chuckles sheepishly."
                    s "He was a Halloween decoration that we never took down."
                    "Somehow that's more mundane an explanation than I was expecting."
                    s "Anyway, let me know if anything else catches your eye."
                    s "We got some postcards, mugs, shirts, some soaps... Carved those myself, by the way."
                    "I look at the carved soaps. There were similar ones in the bathroom of our motel room."
                    "Each one is carved crudely into various shapes. Coyotes, horses, rabbits, trees from the local forest..."
                    "On closer examination it's clear that there are little details that Scott put time and effort into."
                    "Ridges are etched into the soap in areas where an animal's fur is thicker, or to denote the texture of the trees."
                    menu:
                        "Ask about his carvings.":
                            player "These are really good. Where'd you learn to carve like this?"
                            "He smiles bashfully."
                            s "Oh uh, thanks! It was... Well."
                            s "My dad showed me how, when I was a kid. Wood carving though, not soap. It works a lot differently."
                            s "I guess I moved over to soap once we got the motel."
                            "He shrugs a bit, fidgeting with the hem of his flannel shirt."
                            "After a moment, he clears his throat and nods to me."
                            s "I'll throw in a second one for the price of one, if you're looking to buy. Lotta folks who blow through don't ask about it."
                            s "I appreciate the interest."
                            player "Well... Thanks."
                            "He nods quickly."
                        "Move on to something else.":
                            pass
                    s "Oh- By the way, how much of the town have you seen?"
                    player "Barely any of it."
                    s "Looking for a tour? I don't know how long you plan on staying, but I could show you a few spots."
                    "That could be a way to spend the day. I'm not sure what there is to see or do here."
                    menu:
                        "Spend today with Scott.":
                            player "Sure. I could use a tour guide."
                            "He smiles, wheeling himself out from behind the counter."
                            s "Alright, let's get going then."
                            $ monevent = "Scott"
                            jump scottmon
                        "Keep exploring for now.":
                            player "Let me get back to you on that."
                            s "No worries! I'll be here."
                "Talk" if scotttalkedto == 1:
                    menu:
                        s "\"How're you feeling about that tour offer?\""
                        "\"Sure, I'd really like that.\"":
                            "He smiles, wheeling himself out from behind the counter."
                            s "Alright, let's get going then."
                            $ monevent = "Scott"
                            jump scottmon
                        "\"Hold on, I need to do something.\"":
                            s "\"No worries! I'll be here.\""
                "Leave":
                    s "\"Appreciate the visit!\""
            hide scott
            call screen movement()
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---LIZ--- #
        #
    label lizdialogue:
        scene bg [currentloc] [currenttime]
        show liz
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            menu:
                "Liz reads her magazine intently."
                "Talk" if liztalkedto == 0:
                    $ liztalkedto = 1
                    l "\"Your friend left in a hurry.\""
                    player "\"Yeah, he gets like that when he's hungry.\""
                    l "\"Oh, trust me, I do too.\""
                    l "\"Mike told me about your weird plant van. Don't worry about it, that happens all the time around here.\""
                    player "\"What? Really?!\""
                    l "\"Psh, no.\""
                    "She cracks a sly smirk, closing her magazine to look at me and lowering her voice dramatically."
                    menu:
                        l "\"Don't be surprised if people start talking to you about the Coyote Creek Monster, though.\""
                        "\"I really do not care about a monster.\"":
                            l "\"Geez, you sound like that asshole detective.\""
                            $ lizpoints -= 1
                        "\"That sounds cool as hell.\"":
                            l "\"It summons plants and shit.\""
                            $ lizpoints += 1
                    l "\"Dad used to tell me and Scott stories about it when we were kids. Obviously they're just silly stories, but...\""
                    l "\"I dunno. Stuff like that always feels kind of real when you're a kid.\""
                "Talk" if liztalkedto == 1:
                    if lizpoints == 1:
                        l "\"Let me know if you need anything.\""
                        l "\"Talk to you later, [name].\""
                    elif lizpoints == -1:
                        "Liz keeps looking at her magazine."
                "Leave":
                    pass
            hide l
            call screen movement()
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return   
        #
        # ---JULIE--- #
        #
    label juliedialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---ROSA--- #
        #
    label rosadialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---BRANDY--- #
        #
    label brandydialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---LORI--- #
        #
    label loridialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---MARIE--- #
        #
    label mariedialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---BILLY--- #
        #
    label billydialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---HERNANDEZ--- #
        #
    label hernandezdialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---HASTIIN--- #
        #
    label hastiindialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---JOAQUIN--- #
        #
    label joaquindialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---JAVIER--- #
        #
    label javierdialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
           return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---RILEY--- #
        #
    label rileydialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            return
        #
        # ---TUESDAY--- #
        #
        elif currentday == "Tuesday":
            return
        #
        # ---WEDNESDAY--- #
        #
        elif currentday == "Wednesday":
            return
        #
        # ---THURSDAY--- #
        #
        elif currentday == "Thursday":
            return
        #
        # ---FRIDAY--- #
        #
        elif currentday == "Friday":
            return
        #
        # ---SATURDAY--- #
        #
        elif currentday == "Saturday":
            return
        #
        # ---SUNDAY--- #
        #
        elif currentday == "Sunday":
            return
        #
        # ---ROMANTIC EVENTS--- #
        #
label romanticevents:
        #
        # ---NORMAN--- #
        #
    label normanevents:
        label normanmon:
            
            return
        label normantue:
            
            return
        label normanwed:
            
            return
        label normanthu:
            
            return
        label normanfri:
            
            return
        label normansat:
            
            return
        #
        # ---MIKE--- #
        #
    label mikeevents:
        label mikemon:
            
            return
        label miketue:
            
            return
        label mikewed:
            
            return
        label mikethu:
            
            return
        label mikefri:
            
            return
        label mikesat:
            
            return
        #
        # ---KESSLER--- #
        #
    label kesslerevents:
        label kesslermon:
            return
        label kesslertue:
            
            return
        label kesslerwed:
            
            return
        label kesslerthu:
            
            return
        label kesslerfri:
            
            return
        label kesslersat:
            
            return
        #
        # ---SCOTT--- #
        #
    label scottevents:
        label scottmon:
            scene black
            "Scott greets Liz as we head out, passing through the motel parking lot and making our way to the main street."
            scene bg mainstreet day
            "The streets are dusty with desert sand. Evergreen trees stretch upward in the distance, marking the presence of a forest."
            "I keep pace behind Scott on the sidewalk as he leads me through town, gesturing to various locations as we pass."
            show scott
            s "O'Reilly's is pretty much the only place in town to get a drink, if that's your speed."
            s "Ah. Town hall's right here too. That's where you'd find the mayor."
            "He looks up, above the rooftops, and gestures to the trees."
            s "We're actually right next to a national forest here."
            player "I didn't think the Kaibab came out this far. At least not on my maps."
            "Scott shakes his head."
            s "It doesn't. That's Coyote Creek National Forest."
            "Weird. I don't remember reading about that."
            s "It's lesser-known and pretty small."
            s "The district ranger used to visit us a lot..."
            "He goes quiet suddenly, eyes scanning the street as if searching for something else to talk about."
            menu:
                "\"Used to? Not anymore?\"":
                    "He bristles slightly as I say that."
                    s "Well, uh... He was a friend of my dad."
                    s "Not really around anymore. That's all."
                    "The atmosphere is tense now. I feel like it's a sore subject."
                "\"District ranger?\"":
                    $ scottpoints += 1
                    "He releases a breath."
                    s "That'd be Javier Carillo. Tall guy, serious face. Usually in his field uniform. Easy to spot."
                    s "He's usually over at O'Reilly's later in the evening."
            hide scott
            "We spend a while checking out various places around town and chatting."
            "Eventually though, we start to get hungry."
            scene bg diner day
            "We make our way to the diner, and I open up the door to see Norman in one of the booths."
            "He grins, waving me over."
            show norman
            n "[name]! You need to try one of these burgers."
            show norman at left
            show scott
            s "I usually go for the pizza."
            "A young woman in a uniform scoffs as she passes by, lightly tapping Scott on the shoulder and placing a milkshake down on Norman's table."
            show brandy
            unknown "You're the only one who does, Scotty. Rosa's burger is legendary."
            s "I know, I know, I have no taste."
            "She smirks, flipping open her notepad."
            unknown "Damn right. What can I get you boys?"
            s "You know me, Brandy. The usual."
            b "Uh huh. What about you?"
            "She turns to me expectantly."
            menu:
                "Burger.":
                    $ normanpoints += 0.5
                    "Brandy chuckles, and Norman flashes a smile my way."
                    "Scott shakes his head and sighs dramatically, though his attempt at feigning sadness is rendered unsuccessful by his grin."
                    s "Some day it wont be just me."
                "Pizza.":
                    $ scottpoints += 0.5
                    $ pizza = True
                    "Scott laughs, throwing both fists up in triumph. Norman chuckles, and Brandy rolls her eyes."
                    s "See? It's not just me!"
            b "Mhm, whatever you say."
            "She smirks again, jotting down my order."
            b "We'll have that out soon."
            s "Thanks, Brandy."
            hide brandy
            "She heads toward the kitchen, leaving me with Scott and Norman."
            "Norman takes a sip of his milkshake and nods to Scott."
            n "Thanks again for those maps, by the way."
            s "Sure, happy to help. Are you guys staying in town for long?"
            n "The repair guy's ripping pine needles out of my engine block, so... Who knows?"
            n "Shouldn't be more than a few days, right?"
            player "I haven't gotten around to the specifics on that with Mike yet."
            n "I'll talk to him later. Damn, I don't even wanna think about what it's gonna cost."
            "Scott looks between us, confusion written on his face."
            s "Pine needles?"
            "Norman leans forward in his seat, eyes wide."
            n "Dead serious man, the engine was full of plants. No joke."
            s "What, did you drive through the forest or something?"
            "Norman frowns, shaking his head."
            n "Nah, we didn't touch the forest. It's all been desert, we've been on the highway for a while."
            "Fascination overtakes Scott's face."
            s "That's crazy."
            show brandy
            "Conversation continues, and Brandy returns with our food."
            "The pizza is probably the greasiest I've ever seen. Scott's eyes light up at the sight of it."
            s "Very nice. Say thanks to Rosa for me."
            if pizza:
                "My own plate houses a similarly greasy pizza slice that smells heavily of molten cheese. I need to use a handful of napkins to pick it up."
                b "And a pizza slice for you. Enjoy."
            else:
                "My own plate houses a burger encased in fresh, hot frybread. The smell of cooked beef patty and various peppers wafts upward."
                b "Rosa's Navajo burger. Enjoy."
            hide brandy
            hide norman
            hide scott
            "We dig in, talking idly between bites. Eventually, Norman excuses himself to head to the bathroom."
            "Scott expresses a particular interest in our problem."
            show scott
            s "How did the plants get into the engine?"
            player "I was asleep in the back, but Norm woke me up. Must have been a few miles out on the highway."
            s "You pushed the van all that way?"
            "I feel exhausted just thinking about it. Norman had gone downstairs and bought at least six water bottles once we got settled in the motel."
            "Actually, he would have bought those from Scott, now that I think of it."
            player "Yeah... Still feeling the ache from that."
            "He smiles apologetically."
            s "Ouch..."
            if scottpoints >= 2:
                "He seems to think for a moment, chewing on a mouthful of pizza."
                s "Hey. Let's head over to O'Reilly's tonight. My treat. Maybe some relaxation would be good."
                s "If you'd rather not, that's fine, but the offer's on the table."
                player "Thanks, Scott. I'll think about it."
            show norman
            "It's at that moment that Norman bursts into the room loudly, looking shaken."
            player "Norm...?"
            n "Th... I... There's plants everywhere!"
            s "What?!"
            scene bg bathroom
            "... What the fuck?"
            player "This is exactly what our engine was like!"
            show norman
            n "I was washing my hands and it just appeared out of nowhere!"
            show scott
            s "What in the..."
            unknown "What's happening in there?"
            s "Shit... That's Rosa."
            n "I didn't do this!"
            show rosa
            "A woman in an apron appears in the doorway, who I assume to be Rosa."
            ro "Scott?"
            "We all stand there dumbly as she slowly takes in the sight of what has happened to her diner's bathroom."
            "Shock turns to confusion turns to hurt."
            ro "... I'm going to call Gabriela. Wait outside, please."
            scene bg diner day
            show norman
            show scott
            "We spend the next few minutes in tense confusion, waiting for the Chief of Police to arrive."
            show hernandez
            "It's intimidating to see her roll up in her cruiser. We have no way to explain how this happened."
            "Norman especially looks nervous."
            he "Chief Hernandez. Coyote Creek Police Department."
            s "Listen, Chief, I don't think it was either of these guys. There's no way."
            he "Slow down, Cooper. What happened?"
            show rosa
            ro "I hear yelling from the bathroom, I walk in and..."
            ro "Just... Look. I cannot explain."
            "Hernandez sighs, making her way to the scene."
            scene black
            "She interviews all of us. There's not much to say. It's as unexplainable as what happened to our engine."
            "I don't think she trusts us. Especially since Norman was the one to find both."
            scene bg motelroom night
            call screen movement()
            return
        label scotttue:
            
            return
        label scottwed:
            
            return
        label scottthu:
            
            return
        label scottfri:
            
            return
        label scottsat:
            
            return
            