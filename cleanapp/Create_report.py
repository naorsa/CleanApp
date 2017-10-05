import os
from django.shortcuts import render
from reportlab.lib.enums import TA_RIGHT,TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, Spacer, Image,Table
from .models import Reports,Question,Title,UserProfile,CityModel
from reportlab.lib.units import inch
from reportlab.lib import colors
import json
from django.core.mail import EmailMessage



def report(request, reportid):
    pathtocleanapp = os.path.dirname(__file__)
    report = Reports.objects.get(id=reportid)
    testid = str(report.pub_date)
    basename = "report"
    filename = "_".join([basename, testid])
    userid = request.user.id
    user=UserProfile.objects.get(user_id=userid)
    city_ref=CityModel.objects.get(userprofile=user)
    cid = city_ref.id
    cid=str(cid)
    doc = SimpleDocTemplate("cleanapp/reports/"+cid+"_"+filename+".pdf", pagesize=letter, rightMargin=72,leftMargin=72,topMargin=18,bottomMargin=18)
    logo = os.path.join(pathtocleanapp,'Asset 1@2x.png')
    font = os.path.join(pathtocleanapp,'fonts/Nehama.ttf')
    im = Image(logo, 4 * inch, 1 * inch)
    Story = []
    Story.append(im)
    city = report.city
    city = city.City_Name[::-1]
    pdfmetrics.registerFont(TTFont("carmelitbold",font))
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_RIGHT,fontName='carmelitbold'))
    styles.add(ParagraphStyle(name='mytitle', alignment=TA_CENTER,fontName='carmelitbold'))
    styles.add(ParagraphStyle(name='notes', alignment=TA_CENTER,fontName='carmelitbold',textColor=colors.red))
    ptext = '<font size=30>%s</font>' %city
    Story.append(Paragraph(ptext, styles["mytitle"]))
    Story.append(PageBreak())
    titles = Title.objects.order_by('id')
    anses = report.questions_answers
    images = report.questions_images
    anses=json.loads(anses)
    images=json.loads(images)
    for titel in titles:
        questions = Question.objects.filter(title=titel)
        temptitel=str(titel)
        temptitel=temptitel[::-1]
        ptext = '<font size=30>%s</font>' % temptitel
        Story.append(Paragraph(ptext, styles["mytitle"]))
        Story.append(Spacer(1, 12))
        for q in questions:
            qid = q.id
            if q.title == titel:
                q = str(q)
                q = q[::-1]
                qid = str(qid)
                answer=anses[qid]
                imag = images[qid]
                if answer=='1':
                    ansimage = os.path.join(pathtocleanapp,'images/Screen Shot 2017-09-04 at 21.05.20.png')
                    im = Image(ansimage, 2 * inch, 1 * inch)
                elif answer=='2':
                    ansimage = os.path.join(pathtocleanapp,'images/Screen Shot 2017-09-05 at 00.31.50.png')
                    im = Image(ansimage, 2 * inch, 1 * inch)
                elif answer=='3':
                    ansimage = os.path.join(pathtocleanapp,'images/Screen Shot 2017-09-05 at 00.32.40.png')
                    im = Image(ansimage, 2 * inch, 1 * inch)
                elif answer=='4':
                    ansimage = os.path.join(pathtocleanapp,'images/Screen Shot 2017-09-05 at 00.33.02.png')
                    im = Image(ansimage, 2 * inch, 1 * inch)
                else:
                    answer = answer[::-1]
                    ptext = "<font size=30>%s</font>" % answer
                    im = Paragraph(ptext, styles["notes"])
                ptext = "<font size=30>%s</font>"%q
                p=Paragraph(ptext, styles["Justify"])
                data=[[im,p]]
                table = Table(data, colWidths=3.2 * inch)
                table.setStyle([("VALIGN", (0, 0), (-1, -1), "CENTER")])
                Story.append(table)
                Story.append(Spacer(1, 12))
                if imag!='media/uploads/No_image_3x4.svg.png':
                    im = Image(imag, 4 * inch, 3 * inch)
                    Story.append(im)
        Story.append(PageBreak())
    doc.build(Story)
    email = EmailMessage("my subject","My body","cleanapp", ["paul@polo.com","Or@refael-t.co.il"])
    attachment = open("cleanapp/reports/"+cid+"_"+filename+".pdf", 'rb')
    email.attach('myfile.pdf', attachment.read(),'application/pdf')
    email.send()
    return render(request, 'cleanapp/base.html')