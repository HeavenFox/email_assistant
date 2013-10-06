import time_parser
import util

s = ["Wednesday, October 2nd at 1:30pm-2:30pm at Cornell University Career Services, 201 Carpenter Hall"]
s.append("Wednesday 1:30pm to Thursday 2:30am")
s.append("Please complete the following by Friday September 27th at 5:00pm")
s.append("Friday: 3-4pm")
s.append("""
        Your interview for the Software Engineering internship role is confirmed for Wednesday, October 2nd at 1:30pm at Cornell University Career Services, 201 Carpenter Hall. Please arrive 10-15 minutes prior to your interview time and meet with Amy Yeung when you arrive.

        **Please confirm that you have received this email**

        You will speak with two Google engineers for 45 minutes each. Dress is casual--we believe you can be serious without a suit! Again, please review our Software Engineering interview prep doc we have put together for you to get a better understanding of technical concepts and fundamentals you should review to feel prepared.

        Additionally, please check out our YouTube channels for more information about Google and our hiring process:
        Life at Google
        Interviewing at Google

        If you receive any offer deadlines, please let me know. Lastly, should there be a scheduling conflict or an emergency, please notify me as soon as possible. I will contact you within two weeks after your interviews to discuss next steps.
        """)
s.append("""
        Hey Everyone,

        As I mentioned yesterday in Chapter, we are founding the Undergraduate Endowment Committee (UEC) this semester. With a strong foundation in place, the DSP Endowment will benefit not only the active Brotherhood, but also our experience as alumni down the road. If you are interesting in taking part in our Fraternity's first steps towards an Endowment, please take several minutes to fill out the attached UEC Application.

        As co-chairs, Jed and I are looking for 5-7 committee members who are as excited as we are about the Endowment. The deadline for the application is Tuesday October 8th at 6:00pm.

        I'm looking forward to hearing your ideas within the application.

        Fraternally,
        Don
        """)
s.append("""
        Hey ctas!

        It appears that a number of us are busy with prelims and other obligations so we have decided to cancel the CTAS BBQ/Picnic. 

        Instead, please meet us in RPCC lobby at 11am on Sunday, September 29th for Brunch. We hope to see you there!

        Best,

        Rick Jean
        Cornell University | Class of 2014
        B.Sc. Applied Economics and Management
        Mobile: 646-648-2503
        Email: rj92@cornell.edu
        """)
for string in s:
    print util.parse(string)

# import pdb; pdb.set_trace()
print util.parse(s[6])
