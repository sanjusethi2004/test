import dominate
from dominate.tags import *

table_headers1 = ['CHECKLIST','STATUS','COMMENTS']
table_headers2 = ['FLOW TYPE', 'SIERRA Ingestion Components', 'Business Line', 'Cs Division', 'STATUS', 'COMMENTS']
checklist = ["Components up", "Databases availability", "Portal availability", "OMB connectivity"]
flow_type = {"Transactions Inbound to SIERRA": [], "Collateral re-use specific data sources inc its refernce data": [], "Ref Data for Transaction": [], "Clearing dependencies": [], "Data for Margin Reporting": [], "Passthrough": [], "Reporting outbound": []}
components_comments = 'All components are up'
database_availability_comments = 'Database available'
portal_comments = 'Portal available'
OMB_comments = 'OMB connection Available'
componenets_status = database_availability_status = 'OK'
database_availability_status = 'OK'
portal_status = 'OK'
OMB_status = 'OK'

def create_email_template(components_comments, database_availability_comments, OMB_comments, portal_comments, componenets_status,database_availability_status, portal_status,OMB_status):
    doc = dominate.document(title='Example Table')

    with doc.head:
        link(rel='stylesheet', href='style.css')
    
    with doc:
        tags.style("body{font-family:Helvetica}")
        tags.style("h1{font-size:x-large}")
        tags.style("h2{font-size:large}")
        tags.style("table{border-collapse:collapse}")
        tags.style("th{font-size:small;border:1px solid gray;padding:4px;background-color:#87CEFA")
        tags.style("td{font-size:small;text-align:center;border:1px solid gray;padding:4px}")  
        h1('hello world!')
        with div(margin="30px"):
            with table(id="first_table", border="1"):
                with thead():
                    with tr():
                        th('SIERRA Reporting Engine health check')
                    with tbody():
                        with tr():
                            for table_head in table_headers1:
                                th(table_head)
                        for check in checklist:
                            with tr():
                                if check == "Components up":
                                    td(check)
                                    if componenets_status != "OK":
                                        td(componenets_status, style="background-color:red")
                                    else:
                                        td(componenets_status, style="background-color:green")
                                    td(componenets_comments)
                                if check == "Portal availability":
                                    td(check)
                                    if portal_status != "OK":
                                        td(portal_status, style="background-color:red")
                                    else:
                                        td(portal_status, style="background-color:green")
                                    td(portal_comments)
                                if check == "OMB connectivity":
                                    td(check)
                                    if OMB_status != "OK":
                                        td(OMB_status, style="background-color:red")
                                    else:
                                        td(OMB_status, style="background-color:green")
                                    td(OMB_comments)
                                if check == "Databases availability":
                                    td(check)
                                    if  database_availability_status != "OK":
                                        td(database_availability_status, style="background-color:red")
                                    else:
                                        td(database_availability_status, style="background-color:green")
                                    td(database_availability_comments)
                            
        
        h1(' ')
        h1(' ')
        h1(' ')
        h1(' ')

        with div(margin="30px"):
            with table(id="second_table", border="1"):
                with thead():
                    with tr():
                        th('SFTR Related feeds')
                    with tbody():
                        with tr():
                            for table_head in table_headers2:
                                th(table_head)
                        for flow in flow_type:
                            with tr():
                                td(flow, rowspan="4", style = "font-size:small;text-align:left;padding:4px")
                                td("GSL", style = "font-size:small;text-align:left;padding:4px")
                                td("EQ SLEB", style = "font-size:small;text-align:left;padding:4px")
                                td("GM", style = "font-size:small;text-align:left;padding:4px")
                                td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                                td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Vision", style = "font-size:small;text-align:left;padding:4px")
                            td("Repo, FI SLEB", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("PSDW", style = "font-size:small;text-align:left;padding:4px")
                            td("Margin Lending, FI SLEB", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("TAPI", style = "font-size:small;text-align:left;padding:4px")
                            td("SLEB,Repo, FI SLEB", style = "font-size:small;text-align:left;padding:4px")
                            td("IWM/SUB", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Collateral re-use specific data sources inc its refernce data", rowspan="7", style = "font-size:small;text-align:left;padding:4px")
                            td("TDT(Reuse Only)", style = "font-size:small;text-align:left;padding:4px")
                            td("X-Business", rowspan="7", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("MDS Data", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("EQ Data", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Debt Data", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("FX rate Data", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Bucket type static Data", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("ISO currency code Ref Data", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Ref Data for Transaction", rowspan="3", style = "font-size:small;text-align:left;padding:4px")
                            td("CDDS Cpty Ref Data(CMS)", style = "font-size:small;text-align:left;padding:4px")
                            td("X-Business", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("CDH reference Data Feed (MII only)", style = "font-size:small;text-align:left;padding:4px")
                            td("Repo", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("TAPI Cpty Ref data Load", style = "font-size:small;text-align:left;padding:4px")
                            td("SLEB, Repo", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Clearing dependencies", rowspan="3", style = "font-size:small;text-align:left;padding:4px")
                            td("LCH SA", style = "font-size:small;text-align:left;padding:4px")
                            td("Repo", rowspan="3", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():    
                            td("LCH LTD", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr(): 
                            td("Eurex", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Data for margin Reporting", rowspan="3", style = "font-size:small;text-align:left;padding:4px")
                            td("LCH SA", style = "font-size:small;text-align:left;padding:4px")
                            td("Repo", rowspan="3", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():    
                            td("LCH LTD", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():    
                            td("Eurex - Margin Report", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Passthrough", rowspan="1", style = "font-size:small;text-align:left;padding:4px")
                            td("Trax(Passthrough) Trax>Markit", style = "font-size:small;text-align:left;padding:4px")
                            td("Repo, FI&EQ SLEB", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Reporting outbound", rowspan="3", style = "font-size:small;text-align:left;padding:4px")
                            td("Markit(forward and response)", style = "font-size:small;text-align:left;padding:4px")
                            td("X-Business", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr():
                            td("Unavista(MIFID II)", style = "font-size:small;text-align:left;padding:4px")
                            td("X-Business", style = "font-size:small;text-align:left;padding:4px")
                            td("GM", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")
                        with tr(): 
                            td("DTCC", style = "font-size:small;text-align:left;padding:4px")
                            td("SLEB, Repo", style = "font-size:small;text-align:left;padding:4px")
                            td("IWM/SUB", style = "font-size:small;text-align:left;padding:4px")
                            td("ONLINE", style = "font-size:small;text-align:left;padding:4px")
                            td(" ", style = "font-size:small;text-align:left;padding:4px")  
  
                         
    with open('index.html', 'w') as file:
        file.write(doc.render())                
    #print(doc)
create_email_template(components_comments, database_availability_comments, OMB_comments, portal_comments, componenets_status,database_availability_status, portal_status,OMB_status)