
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
        # ---Current day--- #
    $ currentday = "Monday"
    $ currenttime = "Afternoon"
        # ---Events done--- #
    $ monevent = "None"
    $ tueevent = "None"
    $ wedevent = "None"
    $ thuevent = "None"
    $ frievent = "None"
    $ satevent = "None"
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
        scene bg southmain afternoon
        with fade
        "Now the van sits on Main Street, with myself and Norman slumped against it in the dust. We both gasp for breath and pass a bottle of water between us, drenched in sweat. The sun is high in the sky and beating down hard."
        "Norman turns to me, a smile on his face in spite of his clear exhaustion, and breathes in relief."
        show n
        with dissolve
        n "\"Are you as hungry as I am right now?\""
        "I am pretty hungry, I notice. I had been too busy pushing the van to realise until now."
        player "\"Yeah, actually. We didn’t get a chance to grab breakfast.\""
        "Norman scans the street slowly, frowning."
        n "\"I’ll see if I can find somewhere we can get some food.\""
        "He furrows his brow and glances toward the van."
        n "\"I don't understand anything about what happened... The engine was perfect.\""
        "He shakes the worry from his face and gives me a small smile, his eyes sparkling."
        n "\"How about you see the mechanic about it. I'll find us some food.\""
        "Before disappearing, he waves over his shoulder and shouts."
        n "\"I’ll try to find a local map too!\""
        hide n
        with dissolve
        "With that, he’s gone, and I’m left alone."
        scene bg garage afternoon
        with fade
        "The air inside the garage is thick with the smell of oil. It’s almost hard to breathe."
        "I hear music from a cassette player on one of the many shelves that line the walls. The only other noise is that of the mechanic himself at work underneath a jacked up car."
        "All I can see of him are his legs, and occasionally his hand reaching for a new tool. He hums to the chorus of the song playing."
        "He pushes himself out from underneath the car and sits up to wipe his forehead, still tapping his foot to the music. He notices me standing there, and stands to greet me with a smile on his face."
        show m
        with dissolve
        "His hair is short, messy and slick with motor oil. From the various patches sewn clumsily onto his jumpsuit, it’s clear that he’s a fan of science fiction."
        "He cleans off his glasses and leans against the car, still smiling at me."
        m "\"Hey, I’m Mike. How can I help you?\""
        player "\"My friend and I actually had our van break down outside of town…\""
        "I hesitate. How do I even explain something like this?"
        player "\"We have a... uh... Strange problem.\""
        "Mike chuckles and gestures to the door behind me."
        m "\"Alright? Let's go see what the problem is.\""
        hide m
        with dissolve
        scene bg southmain afternoon
        with fade
        "Mike follows me out to the van, whistling the tune from his cassette player."
        show m
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
        hide m
        with dissolve
        scene bg motel afternoon
        with fade
        "The motel lobby is way too brightly lit. The decorating in here is tacky, and it’s clear they don’t get a lot of business."
        "Behind the front desk sits a woman with brown hair and light eyes who doesn’t look like she wants to be there at all."
        "She’s flipping through a magazine absentmindedly. I don’t think she’s even noticed I’m here yet."
        show l
        with dissolve
        unknown "\"... Can I help you?\""
        "Yes she has."
        player "\"Uh. I'm looking for a room.\""
        "The woman closes her magazine and tosses it onto the counter in front of her. She opens a drawer and rummages in it for a second before pulling out a ledger and opening it, turning it to face me."
        unknown "\"Rates are listed here. Sign and I'll get you a key.\""
        "I get a room with two beds. The woman hands me a key and picks up her magazine again."
        l "\"Thanks. I'm Liz, by the way. If you need anything I'm usually here. If not, my brother runs the gift store next door.\""
        hide l
        with dissolve
        window show
        scene bg motel afternoon
        with hpunch
        window auto
        "When I turn to check out said gift store, I find myself bumping into someone on their way in."
        show k
        with dissolve
        unknown "\"‘scuse me.\""
        "The man in front of me has dark, curly hair and a scratchy shadow of stubble on his face."
        "He looks at me with tired eyes and nurses the coffee cup in his hand."
        unknown "\"You don't look local. Me neither.\""
        k "\"Detective Kessler, County Sheriff’s Office. I got called in by the chief.\""
        k "\"Town's got some kind of vandalism problem.\""
        "That’s when I notice a small face peek out from behind him."
        show j
        with dissolve
        "Trailing along behind the detective is a young girl who peers up at me cautiously, clutching firmly onto him. Kessler glances down at her."
        k "\"This is Julie, my daughter.\""
        j "\"... Hi.\""
        "Julie tugs on his pants leg urgently, signalling that she does not want to be here right now. The detective sighs and ruffles her hair."
        k "\"I better get moving.\""
        "He grumbles to himself and moves past me, toward the rooms."
        k "\"Be seeing you.\""
        "With that, I’m left in the motel lobby with Liz again, who has evidently not been paying attention to our exchange and doesn’t seem to care."
        hide k
        with dissolve
        hide j
        with dissolve
        scene bg giftstore afternoon
        with fade
        "The souvenirs that line the shelves look like they've been here for months. There's a layer of dust coating each one."
        "Behind the desk sits a man who has fallen asleep in his wheelchair. Like the main section of the motel, this gift shore doesn't seem to get much business."
        "I clear my throat and make my presence known. The man jolts awake and his eyes light up at the sight of a potential customer."
        show s
        with dissolve
        "His relation to Liz is evident in his face. He has the same brown hair and light eyes, though he looks considerably less stern and more uncertain."
        s "\"Welcome to Cooper's Motel & Gift Store! I'm Scott, what can I do for you?\""
        player "\"Just looking... I'm [name]. I'm new in town and thought I'd introduce myself.\""
        "He looks a bit let down, but quickly regains his cheery composure."
        s "\"Pleasure to meet you! It's rare to see fresh faces in Coyote Creek... It's a shame, really. This town has a lot of charm.\""
        "He glances back at the objects on display and frowns."
        s "\"... It really is an underrated place.\""
        "He snaps out of it and looks back at me, his smile returning to his face."
        s "\"I hope you like it here. Feel free to drop by whenever you want. I've always got time.\""
        hide s
        with dissolve
        scene black
        "Norm's van is, for lack of a better term, completely fucked."
        "... It looks like we'll be sticking around here for at least a week while it gets fixed."
        "I have my doubts that anything of note will happen while we're here, but..."
        scene title
        "... Maybe I'll find myself surprised."
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
        scene bg motelroom morning
        with fade
        show n
        with dissolve
        player "\"Ugh... What time is it?\""
        n "\"Eight. The diner's doing a breakfast deal, come on.\""
        "I close my eyes again. Norman immediately groans."
        n "\"Y'know what? Alright. I'll be there. Get up whenever you're ready.\""
        hide n
        with dissolve
        "Before I have a chance to reply, he hurries out of the room and closes the door behind him."
        show screen date("Monday, June 23rd", "Morning")
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
        show screen date("Tuesday, June 24th", "Morning")
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
        show screen date("Wednesday, June 25th", "Morning")
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
        show screen date("Thursday, June 26th", "Morning")
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
        show screen date("Friday, June 27th", "Morning")
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
        show screen date("Saturday, June 28th", "Morning")
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
        show screen date("Sunday, June 29th", "Morning")
        "... It's time to go home."
        scene bg motelroom morning
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
        if currentday == "Monday" && currenttime == "Morning":
            menu:
                n "\"Something you need, [name]?\""
                "Talk" if normantalkedto == 0:
                    "Norman tilts his head in greeting."
                    n "\"Finally out of bed?\""
                    player "\"Mmhm… You seemed excited about this place.\""
                    n "\"What can I say? I like trying new food.\""
                    player "\"Does it bother you that we're stuck here?\""
                    n "\"Nah. It's just another adventure, right?\""
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
        elif currenttime == "Evening":
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
        if currentday == "Monday" && currenttime == "Morning":
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
                            k "\"... Okay? Why not.\""
                            k "\"Don't tell nobody I'm letting you come along though.\""
                            $ monevent == "Daniel"
                            jump kesslermon
                        "\"See you later.\"":
                            "Mmhm."
                    jump kesslerdialogue
                "Leave":
                    "Kessler nods."
                    return
        elif currenttime == "Evening" && monevent == "Daniel":
            k "\"Thanks for tagging along today, [surname].\""
            k "\"It's not protocol, but... Figured it wouldn't hurt. Not like you're a suspect.\""
            player "\"Why did you let me come along, anyway?\""
            "He shrugs."
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
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            menu:
                s "\"Hey, Mr. [surname], welcome!\""
                "Talk" if scotttalkedto == 0:
                    player "\"Uh. What is that on the wall.\""
                    s "\"What, you mean the skeleton? That's Buffalo Bones, don't worry about it. He's great.\""
                    player "\"Um.\""
                    menu:
                        s "\"So what's your first impression of Coyote Creek? I was actually going to ask if you wanted a quick tour.\""
                        "\"It's kind of a dump.\"":
                            $ scottpoints -= 0.5
                            "He deflates."
                            s "\"That's a shame.\""
                        "\"Seems alright so far.\"":
                            $ scottpoints += 0.5
                            s "\"Glad you think so!\""
                    jump scottdialogue
                "Spend today with Scott" if scotttalkedto == 1:
                    menu:
                        s "\"How're you feeling about that tour offer?\""
                        "\"Sure, I'd really like that.\"":
                            s "\"Let's get going then!\""
                            $ monevent = "Scott"
                            jump scottmon
                        "\"Hold on, I need to do something.\"":
                            s "\"No worries!\""
                            return
                    jump scottdialogue
                "Leave":
                    s "\"Appreciate the visit!\""
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
        # ---LIZ--- #
        #
    label lizdialogue:
        #
        # ---MONDAY--- #
        #
        if currentday == "Monday":
            menu:
                "Talk" if liztalkedto == 0:
                    $ liztalkedto = 1
                    l "\"Your friend left in a hurry.\""
                    player "\"Yeah, he gets like that when he's hungry.\""
                    l "\"Oh, trust me, I do too.\""
                    l "\"Mike told me about your weird plant van. Don't worry about it, that happens all the time around here.\""
                    player "\"What? Really?!\""
                    l "\"Psh, no.\""
                    menu:
                        l "\"Don't be surprised if people start talking to you about the Coyote Creek Monster though.\""
                        "\"I really do not care about a monster.\"":
                            l "\"Geez, you sound like that asshole detective.\""
                            $ lizpoints -= 1
                        "\"That sounds cool as hell.\"":
                            l "\"Yeah, it's pretty cool. It summons plants and shit.\""
                            $ lizpoints += 1
                    l "\"Dad used to tell me and Scott stories about it when we were kids. Obviously they're just silly stories, but...\""
                    l "\"I dunno. Stuff like that always feels kind of real when you're a kid.\""
                    jump lizdialogue
                "Talk" if liztalkedto == 1:
                    if lizpoints == 1:
                        l "\"Talk to you later, [name].\""
                    elif lizpoints == -1:
                        "Liz keeps looking at her magazine."
                    jump lizdialogue
                "Leave":
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
            "Kessler drains his coffee and wordlessly heads outside, signalling that I should follow with a subtle tilt of his head."
            "In front of the station sits his patrol vehicle, a Crown Vic with the symbol of the County Sheriff’s Office emblazoned on the doors."
            "He takes a moment to fish his keys from his pocket, grumbling in annoyance, before opening the door and taking a seat. I follow suit."
            k "\"... What brings you to Coyote Creek?\""
            player "\"It's a bit weird...\""
            "He shrugs and turns the key in the ignition, starting up the car. He pulls out onto the road and turns to head deeper into the town."
            player "\"My friend’s van broke down. We’re on a road trip.\""
            k "\"Sounds straightforward.\""
            player "\"Well, yeah but. The engine is full of plants.\""
            "Kessler glances toward me before turning his eyes back to the road."
            k "\"I might want a look at that engine, if you don’t mind.\""
            player "\"You’d have to ask Norman. It’s his baby.\""
            k "\"That your friend? Alright.\""
            player "\"There's also the issue of it being looked at by the mechanic right now...\""
            k "\"Yeah, I'll talk to Nez.\""
            "After a short journey, the car rolls to a stop, and Kessler pulls the handbrake."
            k "\"We're here.\""
            "We step out of the car, into the parking lot of Coyote Creek High. School is clearly out for the summer, and there’s only one other car here; A local police vehicle."
            k "\"See, about your plant problem... Turns out, something happened similar to that, right here.\""
            k "\"Nobody can figure out for shit what happened or how the plants got there. Gonna give the place a once-over.\""
            k "\"Also, whoever did it stole the mascot too.\""
            player "\"... Why would someone steal the mascot?\""
            k "\"I don’t know. I’ve seen pictures. He’s a scary bastard, I wouldn’t want to steal him.\""
            "He locks the car and heads toward the front door of the school."
            player "\"So what would make you want to steal a mascot, personally? You did just sort of imply that there is a situation where you would do that.\""
            "I think I see a smile flash across his face momentarily."
            k "\"Hm. I’ll have to get back to you on that.\""
            "We enter the gym of Coyote Creek High, where a woman in a police uniform waits. She looks unimpressed."
            unknown "\"Took your damn time, Detective.\""
            "She notices me and her eyes narrow even more."
            unknown "\"... Who’s this guy?\""
            k "\"Don’t worry about it, Chief. Just an out-of-towner.\""
            "I’ve never seen anyone look more exasperated."
            unknown "\"I can {i}see{/i} that, I mean {i}what is he doing here?{/i}\""
            "The detective shrugs."
            unknown "\"...\""
            he "\"Chief Gabriela Hernandez. Try not to get in the way.\""
            k "\"Right... Okay. So. What are we lookin' at here?\""
            "Kessler gestures to the mess that is the gym. The ground is littered with vines. Hernandez sighs and shakes her head, looking dumbfounded."
            he "\"If I knew what we were lookin' at I wouldn't have called in a county detective...\""
            he "\"All I know is that I can't figure out who's behind this, or why someone would do this in the first place.\""
            "I take a closer look at the vines, noting their familiarity."
            player "\"They do look similar to what we found in Norm's engine...\""
            k "\"Interesting... When did you notice them?\""
            "He watches me with intent focus. I have to tear my eyes away from him."
            player "\"We were near the edge of the forest. Had to push it all the way into town. This was yesterday morning.\""
            k "\"Huh. Must've happened while you were stopped.\""
            player "\"I uh... Was asleep. Norman could probably tell you more details.\""
            "Kessler nods, shooting a glance to Hernandez."
            k "\"Got any suspects?\""
            he "\"Well... I did find something.\""
            "She produces an evidence bag. In it is a single worn-out sneaker."
            he "\"Someone left here in a rush. Lost their shoe. We find the owner and I think we've got ourselves a lead.\""
            "Kessler grunts in acknowledgement, scanning the room thoughtfully. His eyes settle on one of the windows, left wide open."
            k "\"... That open when it was reported?\""
            he "\"Uh huh. Caretaker swears to God it was shut when he left last night, though.\""
            he "\"I think that's the point of exit, but not entry. The gym door is locked with a padlock usually, but that was on the ground outside.\""
            "Kessler is just staring at the plants on the ground."
            k "\"... I mean.\""
            k "\"I just don't get the {i}why{/i} in this situation, you know? I can get some kid busting in and stealing a mascot, but...\""
            he "\"The weird plants, yeah. Agreed.\""
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
            