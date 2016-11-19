import json
import urllib2

# question 2
my_json = urllib2.urlopen('http://openstates.org/api/v1/bills/?state=mo&chamber=upper&search_window=session:2016').read()

data = json.loads(my_json)

id_list = []

for bills in data:
    id_list.append(bills["id"])

for i in id_list:
    link = "http://openstates.org/api/v1/bills/" + i
    bill_json = urllib2.urlopen(link).read()
    bill_data = json.loads(bill_json)
    print bill_data["title"], bill_data["actions"][-1]["action"]

# Modifies provisions relating to health care Signed by Governor
# Modifies provisions relating to health care Vetoed by Governor
# Modifies various provisions regarding palliative care, the Board of Pharmacy, pharmacists, health insurance, and pharmacy benefit managers Signed by Governor
# Modifies various provisions relating to hospitals, physical therapists, and medication Signed by Governor
# Modifies several provisions relating to health care providers Signed by Governor
# Modifies provisions relating to financial transactions Signed by Governor
# Modifies provisions relating to transportation facilities Signed by Governor
# Modifies provisions relating to victims of crime Signed by Governor
# Modifies provisions relating to intoxicating liquor Signed by Governor
# Modifies provisions relating to bonded entities Signed by Governor
# Modifies provisions relating to alcohol Vetoed by Governor
# Allows the State Auditor to audit community improvement districts Signed by Governor
# Allows an individual to deduct income earned through active military duty from their Missouri adjusted gross income Signed by Governor
# Modifies provisions relating to expert witnesses Vetoed by Governor
# Creates an income tax deduction for payments received as part of a program that compensates agricultural producers for losses from disaster or emergency Vetoed by Governor
# Modifies provisions relating to sales tax Signed by Governor
# Creates a sales tax exemption for parts of certain types of medical equipment Signed by Governor
# Modifies provisions relating to the collateral source rule and provides that parties may introduce evidence of the actual cost, rather than the value, of the medical care rendered Vetoed by Governor
# Modifies provisions relating to livestock trespass liability Vetoed by Governor
# Exempts instructional classes from sales tax Vetoed by Governor
# Modifies provisions relating to county sheriffs, self defense, unlawful use of weapons, and concealed carry permits Vetoed by Governor
# Repeals the Advisory Council to the Director of the Missouri Agriculture Experiment Station and establishes the Fertilizer Control Board Signed by Governor
# Modifies provisions relating to motor vehicles Signed by Governor
# Modifies corporate registration report requirements for authorized farm corporations and family farm corporations Signed by Governor
# Modifies provisions relating to agriculture Signed by Governor
# Designates two memorial highways in Boone County Signed by Governor
# Designates the "Trooper James M. Bava Memorial Highway" Signed by Governor
# Contains provisions relating to fire protection, sheltered workshops, assessments of mining property, consolidation of road districts, and property managers Vetoed by Governor
# Designates the month of September as Suicide Prevention Awareness Month Signed by Governor
# Creates regulations for insurance requirements for transportation network companies and transportation network company drivers Signed by Governor
# Modifies several provisions relating to elementary and secondary education Signed by Governor
# Modifies various provisions regarding municipalities located in St. Louis County, nuisance abatement ordinances, disincorporation procedures for various cities, and municipal courts Signed by Governor
# Authorizes the conveyance of certain state properties Signed by Governor
# Establishes several provisions relating to higher education Signed by Governor
# Changes the effective date of the repeal and enactment of certain provisions of the Uniform Interstate Family Support Act Signed by Governor
# Requires thirty minutes of cardiopulmonary resuscitation instruction and training during high school Signed by Governor
# Modifies composition of the Career and Technical Education Advisory Council and requires said council to establish minimum requirement for a career and technical education certificate Signed by Governor
# Modifies several provisions relating to higher education financial aid for members of the military and their families Signed by Governor
# Modifies provisions relating to infection reporting of health care facilities and telehealth services Signed by Governor
# Allows a pharmacist to select an interchangeable biological product when filling a biological product prescription Signed by Governor
# Modifies the crimes of stealing and fraudulent procurement of a credit or debit device Signed by Governor
# Modifies provisions of law relating to bidding procedures for county depositaries Signed by Governor
# Allows the court to order a wireless service provider to transfer the rights of a wireless telephone number to a petitioner under certain circumstances Signed by Governor
# Modifies provisions relating to public assistance programs Delivered to Governor
# Modifies the law relating to unemployment compensation benefits Delivered to Governor
# Modifies the law relating to workers' compensation premium rates Delivered to Governor
# Modifies provisions related to first degree murder Delivered to Governor
# Modifies provisions relating to law enforcement officers and political subdivisions Delivered to Governor
# Modifies laws relating to the Court Automation Fund, the Basic Legal Services Fund, and public defenders Delivered to Governor
# Modifies provisions relating to petitions for the expungement of criminal records Delivered to Governor
# Designates certain state highways and creates a process for the naming of additional highways and bridges Delivered to Governor
# Modifies the law relating to the prosecution of election offenses Delivered to Governor
# Allows certain circuits to appoint an additional court marshal, authorizes an additional judge in certain circuits, excludes firearms from bankruptcy, and establishes the Missouri Commercial Receivership Act Delivered to Governor
# Modifies numerous provisions relating to public safety Delivered to Governor
# Enacts new provisions of law relating to the workers' compensation insurance premiums of volunteer fire departments Delivered to Governor
# Designates certain memorial infrastructure Delivered to Governor
# Modifies provisions relating to abortion, including donation of fetal tissue, tissue reports, physician privileges, and ambulatory surgical center licensing and inspections Informal Calendar S Bills for Perfection--SB 644-Onder, with SCS
# Modifies provisions relating to construction H Calendar Senate Bills for Third Reading w/HCS
# Establishes a nursing compact, physical therapy compact, and legislative procedures for regulating professions, and modifies provisions regarding medical hemp extract, land surveyors, collaborative practice, and the nurse education incentive program H Calendar Senate Bills for Third Reading w/HCS
# Establishes requirements for authorized entities to stock epinephrine (EPI) auto-injectors for use in emergencies In Conference--SB 677-Sater, with HCS, as amended
# Modifies provisions relating to land purchases made on behalf of state departments H Calendar Senate Concurrent Resolutions for Third Reading w/HCS
# Creates a sales tax exemption for fitness facilities, gyms, and dance studios Informal Calendar S Bills for Perfection--SB 706-Dixon
# Modifies provisions relating to the regulation of motor vehicles H Calendar Senate Bills for Third Reading w/HCS
# Repeals the death penalty Informal Calendar S Bills for Perfection--SB 816-Wieland, et al
# Prohibits abortions performed solely because of a prenatal diagnosis, test, or screening indicating Down Syndrome or the potential of Down Syndrome in an unborn child Informal Calendar S Bills for Perfection--SB 802-Sater
# Modifies provisions relating to construction contracts entered into by political subdivisions Informal Calendar S Bills for Perfection--SBs 789 & 595-Wasson, with SCS
# Modifies provisions relating to healthcare In Conference--SS for SB 621-Romine, with HCS, as amended
# Implements the Streamlined Sales and Use Tax Agreement Formal Calendar S Bills for Perfection--SB 795-Wallingford, with SCS
# Modifies provisions relating to agriculture In Conference--SCS for SB 703-Munzlinger, with HCS, as amended
# Modifies retirement benefits for newly elected members of the General Assembly and statewide officials Informal Calendar S Bills for Perfection--SB 680-Emery
# Requires that municipalities in the St. Louis County sales tax pool receive at least 50% of the revenue generated inside a given municipality Formal Calendar S Bills for Third Reading--SS for SCS for SB 788-Schatz (In Fiscal Oversight)
# Contains provisions relating to political subdivisions, wireless facilities, Department of Transportation vehicles, limited liability companies, and circuit court judges S Bills with H Amendments--SB 676-Sater, with HCS, as amended
# Establishes the Civil Litigation Funding Act Informal Calendar S Bills for Perfection--SB 785-Schaefer, with SCS, SS for SCS, SA 1, SSA 1 for SA 1, SA 1 to SSA 1 for SA 1 & point of order (pending)
# Modifies how fourth class cities may proceed with road improvements Informal Calendar S Bills for Perfection--SB 686-Wallingford, with SCS
# Authorizes telephone companies to elect to have their tangible personal property assessed in accordance with a depreciation schedule Informal Calendar S Bills for Third Reading--SB 783-Onder
# Establishes the Joint Committee on Public Assistance S Bills with H Amendments--SCS for SBs 688 & 854-Romine, with HCS, as amended
# Modifies provisions related to law enforcement officers, inmates, crime, preparation of land descriptions, courts, concealed carry permits, and public defenders S Bills with H Amendments--SS for SCS for SB 663-Dixon, with HCS, as amended
# Contains provisions relating to crimes and criminal court proceedings H Calendar Senate Bills for Third Reading w/HCS
# Modifies the statute specifying when police officers are justified using force H Calendar Senate Bills for Third Reading w/HCS
# Creates the Missouri Uniform Powers of Appointment H Calendar Senate Bills for Third Reading
# Requires voter or General Assembly approval before the Regional Convention and Sports Complex Authority extends or issues new bonds obligating the state Informal Calendar S Bills for Perfection--SB 580-Schaaf, with SCS & SA 2 (pending)
# Provides that the state shall not require maintenance of licensure or any form of specialty medical board certification to practice medicine and modifies examination requirements for physicians Informal Calendar S Bills for Perfection--SB 772-Onder, with SCS
# Repeals a section relating to the expiration date of economic subsidies for Missouri qualified fuel ethanol producers Informal Calendar S Bills for Perfection--SB 825-Munzlinger, with SA 1 (pending)
# Adopts the Compact for a Balanced Budget Informal Calendar S Bills for Perfection--SCS for SBs 662 & 587-Dixon
# Modifies the A+ Schools Program by removing the requirement that the student's attendance of public high school occur in the three years immediately prior to graduation In Conference--SCS for SB 650-Pearce, with HA 1, HA 2, HA 3, HA 4, HA 5, HA 6, HA 7, HA 8, as amended & HA 9 (Further conference granted)
# Modifies the law relating to business fees In Conference--SS for SB 799-Kraus, with HCS, as amended
# Authorizes additional circuit judges for certain circuits when indicated by a judicial performance report and repeals provisions regarding the appointment of a janitor-messenger Informal Calendar S Bills for Perfection--SB 733-Dixon
# Modifies the law relating to the investment policies of the state S Bills with H Amendments--SB 573-Schmitt, with HCS, as amended
# Establishes the Caregiver, Advise, Record, and Enable Act and a physical therapist compact, as well as allows optometry students to train under the supervision of a physician or optometrist H Calendar Senate Bills for Third Reading w/HCS
# Requires the Department of Revenue to pay the taxpayers' attorneys' fees in income tax cases when the taxpayer receives a favorable judgement Informal Calendar S Bills for Perfection--SB 798-Kraus, with SCS
# Allows sheriffs and deputies to assist in other counties throughout the state Informal Calendar S Bills for Perfection--SB 734-Dixon
# Modifies provisions relating to the detention and shackling of juvenile offenders and detention and shackling of pregnant offenders H Calendar Senate Bills for Third Reading w/HCS
# Phases out the St. Louis City earnings tax Informal Calendar S Bills for Perfection--SB 575-Schaefer, with SCS, SS for SCS & SA 1 (pending)
# Repeals certain provisions relating to products liability civil actions Informal Calendar S Bills for Perfection--SB 792-Richard
# Modifies the law relating to initiative petitions Informal Calendar S Bills for Perfection--SJR 23-Sater, with SS (pending)
# Requires a candidate for the office of public administrator to meet the bonding requirements of the office and modifies laws regarding estate administration H Calendar Senate Bills for Third Reading w/HCS
# Modifies the law relating to paper ballots Informal Calendar S Bills for Perfection--SB 771-Onder
# Adds a statutory aggravating circumstance for murder in the first degree for certain acts of terrorism Informal Calendar S Bills for Perfection--SB 775-Schaefer
# Modifies provisions relating to tax increment financing Informal Calendar S Bills for Perfection--SB 805-Onder, with SCS
# Modifies provisions relating to civil actions brought under merchandising practices and products liability provisions of law Informal Calendar S Bills for Perfection--SB 793-Richard
# Prohibits a health carrier or other insurer that writes vision insurance from requiring an optometrist to provide services or materials at a discount that are not covered and reimbursed under the plan Informal Calendar S Bills for Perfection--SB 830-Wasson, with SCS
# Raises taxes on fuels and increases fuel decal fees H Calendar Senate Bills for Third Reading w/HCS (In Fiscal Review)
# Requires all departments and divisions of the state, including statewide offices, to post copies of contracts entered into for the provision of legal services from outside firms on the Missouri Accountability Portal H Calendar Senate Bills for Third Reading w/HCS & HCA 3
# Modifies the gubernatorial appointment process for acting directors and members of boards and commissions Informal Calendar S Bills for Perfection--SB 774-Schmitt
# Provides ways a professional licensee may submit payment and information to a licensing board, establishes legislative procedures for regulating previously unregulated professions and modifies provisions relating to various health care providers S Bills with H Amendments--SB 831-Wasson, with HCS, as amended
# Modifies provisions regarding estate administration and the office of public administrator and establishes the Designated Health Care Decision-Maker Act H Calendar Senate Bills for Third Reading w/HCS
# Modifies provisions relating to registration of certain motor vehicles In Conference--SB 640-Schatz, with HCS, as amended
# Modifies provisions relating to probation and parole H Calendar Senate Bills for Third Reading w/HCS
# Modifies provisions relating to collective bargaining representation for public employees Informal Calendar S Bills for Perfection--SB 806-Onder, with SCS
# Modifies provisions relating to taxation H Calendar Senate Bills for Third Reading w/HCS
# Allows the circuit court in St. Louis City to collect a fee not to exceed twenty dollars, rather than fifteen, to go toward the law library Informal Calendar S Bills for Perfection--SB 812-Keaveny
# Adds the real property of a vineyard and related buildings to the definition of "agricultural and horticultural property" for property tax purposes Informal Calendar S Bills for Perfection--SB 596-Kraus, with SCS
# Requires each public institution of higher education to develop and implement a policy to advise students and staff on available suicide prevention programs In Conference--SB 627-Nasheed, with HA 1, HA 2, HA 3, HA 4, as amended, HA 5 & HA 6 (Further conference granted)
# Modifies several provisions relating to elementary and secondary education H Calendar Senate Bills for Third Reading w/HCS
# Designates the "German Heritage Corridor of Missouri" H Calendar Senate Bills for Third Reading
# Requires the Department of Elementary and Secondary Education to develop training guidelines and school districts to adopt a policy for youth suicide awareness and prevention education H Calendar Senate Bills for Third Reading
# Requires the State Board of Education to develop a simplified annual school report card Informal Calendar S Bills for Perfection--SB 719-Emery, with SCS
# Modifies provisions relating to mine property Informal Calendar S Bills for Perfection--SB 622-Romine, with SCS
# Modifies provisions of the Prosecuting Attorneys and Circuit Attorneys' Retirement System and allows political subdivisions to assign operation of a retirement plan to LAGERS In Conference--SB 639-Riddle, with HCS, as amended
# Establishes the Joint Committee on Capitol Improvements H adopted
# Urges the Department of Higher Education and Department of Health and Senior Services to encourage the dissemination of information about meningococcal disease and its vaccines Resolutions Calendar - Reported from Committee--SCR 54-Walsh
# Declares November 14, 2016, as Neuroblastoma Cancer Awareness Day H adopted
# Authorizes the republishing of the Revised Statutes of Missouri House Calendar Senate Concurrent Resolutions
# Prohibits private nuisance actions from being brought when the property owner has a government issued permit Informal Calendar S Bills for Perfection--SB 894-Munzlinger, with SS (pending)
# Extends a sunset provision for coverage of early refills of prescription eye drops Informal Calendar S Bills for Perfection--SB 868-Wasson
# Provides that a person who removes an unattended child from a locked car shall not be held liable for damages Informal Calendar S Bills for Perfection--SB 896-Hegeman
# Creates property tax valuation freeze for the elderly Informal Calendar S Bills for Perfection--SJR 35-Kraus, with SCS
# Requires referrals for out of state abortions to be accompanied by specified printed materials Informal Calendar S Bills for Perfection--SB 883-Riddle
# Applies to Congress for the calling of an Article V convention of states to propose certain amendments to the United States Constitution which place limits on the federal government Resolutions Calendar - Reported from Committee--SCRs 53 & 44-Schaefer, with SCS
# Creates and funds the Department of Revenue Technology Fund through an administrative fee for notice of lien processing Informal Calendar S Bills for Perfection--SB 898-Cunningham
# Establishes the Advance Health Care Directive Registry H Calendar Senate Bills for Third Reading
# Creates requirements for co-payments and notice of insurance coverage for occupational therapy Informal Calendar S Bills for Perfection--SB 853-Brown
# Suspends state agency activities relating to the Clean Power Plan until a certain stay is lifted, and requires the Department of Natural Resources to submit an extension for submitting a final plan to the EPA upon the Clean Power Plan being upheld in federal court Informal Calendar S Bills for Perfection--SB 858-Romine, with SCS & SS for SCS (pending)
# Prohibits the adoption of any tax increment financing from superseding, altering, or reducing sheltered workshop property tax levies S Bills with H Amendments--SB 869-Schmitt, with HCS, as amended
# Prohibits the release of identifying information of lottery winners and allows victims of human trafficking to participate in the Address Confidentiality Program H Calendar Senate Bills for Third Reading w/HCS
# Modifies provisions relating to emergency communications services Informal Calendar S Bills for Perfection--SB 871-Wallingford
# Provides that only a licensed pharmacist can determine to dispense an emergency supply of medication without the prescriber's authorization and may dispense varying quantities of maintenance medication In Conference--SB 864-Sater, with HCS, as amended
# Allows qualified motorcycle operators to operate motorcycles and motortricycles without protective headgear under certain conditions Informal Calendar S Bills for Perfection--SBs 851 & 694-Brown, with SCS
# Modifies provisions relating to rate schedules authorized for certain utilities outside of general rate proceedings Informal Calendar S Bills for Perfection--SB 848-Emery, with SCS
# Creates the Missouri Science, Technology, Engineering and Mathematics Initiative In Conference--SB 873-Pearce, with HCS, as amended
# Designates certain highways and bridges within the state H Calendar Senate Bills for Third Reading w/HCS
# Removes penalties for taxes paid under protest or as part of a disputed assessment S Bills with H Amendments--SB 897-Hegeman, with HA 1, HA 2, HA 4 & HA 5
# Establishes several provisions relating to financial assistance for dual enrollment courses Formal Calendar S Bills for Third Reading--SCS for SBs 857 & 712-Romine (In Fiscal Oversight)
# Modifies provisions related to elementary and secondary education H Calendar Senate Bills for Third Reading w/HCS
# Designates certain state highways and creates a process for the naming of additional highways and bridges H Calendar Senate Bills for Third Reading w/HCS
# Delineates procedures to be used by pharmacy benefit managers with regards to maximum allowable cost lists Informal Calendar S Bills for Perfection--SB 908-Sater, with SCS
# Modifies definitions in the Missouri Human Rights Act Informal Calendar S Bills for Perfection--SB 916-Schaefer
# Urges Congress to call an Article V Convention for the purpose of proposing amendments to the United States Constitution Resolutions Calendar - Reported from Committee--SCR 55-Holsman
# Adjusts the exemption amount allowed for each dependent based on the Consumer Price Index Informal Calendar S Bills for Perfection--SB 920-Schmitt and Kraus
# Designates May as Cystic Fibrosis Awareness Month Resolutions Calendar - Reported from Committee--SCR 56-Brown
# Extends the authority for regional jail districts to impose a sales tax until September 30, 2027 S Bills with H Amendments--SS for SB 937-Wallingford, with HCS, as amended
# Modifies several provisions relating to higher education H Calendar Senate Bills for Third Reading w/HCS
# Modifies provisions of the Missouri Preneed Funeral Contract Act Informal Calendar S Bills for Perfection--SB 951-Wasson, with SA 1 (pending)
# Modifies provisions of law relating to child custody orders Informal Calendar S Bills for Perfection--SB 964-Wallingford, with SCS (pending)
# Urges the United States Congress to propose the Regulation Freedom Amendment to the U.S. Constitution Resolutions Calendar - Reported from Committee--SCR 59-Emery
# Requires public retirement plans to provide financial information to participants, modifies the criteria for when a public plan is deemed delinquent, and changes the employer and employee contributions for CURP Informal Calendar S Bills for Perfection--SB 980-Keaveny, with SCS, SS for SCS, SA 1 & SA 3 to SA 1 (pending)
# Transfers powers of the Missouri Consolidated Health Care Plan Board to the Office of Administration Informal Calendar S Bills for Perfection--SB 966-Schaaf
# Provides MO HealthNet reimbursement for behavior assessment and intervention Informal Calendar S Bills for Perfection--SB 972-Silvey
# Applies to Congress for the calling of an Article V convention of states to propose an amendment to the United States Constitution regarding term limits for members of Congress Resolutions Calendar - Reported from Committee--SCR 61-Parson
# Allows entertainment facilities to sell alcoholic beverages through the use of mobile applications Informal Calendar S Bills for Perfection--SB 995-Riddle
# Urges a commitment to equal rights for people with cognitive disabilities to access technology and information Resolutions Calendar - Reported from Committee--SCR 60-Curls
# Prohibits political subdivisions from participating in any action in federal court as either a representative or member of a class to enforce or collect any tax Informal Calendar S Bills for Perfection--SB 1003-Onder
# Modifies Supreme Court Rule 52.08 to prohibit political subdivisions from joining certain class actions Informal Calendar S Bills for Perfection--SB 1004-Onder
# Changes the "Farm-to-School Act" and program to the "Farm-to-Table Act" and program and modifies provisions of such program Informal Calendar S Bills for Perfection--SBs 1010, 958 & 878-Curls, with SCS
# Subject to appropriations, requires the Department of Elementary and Secondary Education to subsidize the exam fee for those taking the high school equivalency degree exam for the first time Formal Calendar S Bills for Third Reading--SCS for SB 998-Romine (In Fiscal Oversight)
# Urges the Missouri congressional delegation to support the use of science-based data to assess the impacts and regulation of modern agricultural technologies Resolutions Calendar - Reported from Committee--SCR 63-Curls and Munzlinger
# Modifies several provisions relating to elementary and secondary education In Conference--SCS for SB 996-Pearce, with HCS, as amended
# Modifies the law relating to meningococcal vaccines for students enrolled at public institutions of higher education Informal Calendar S Bills for Perfection--SB 1005-Walsh
# Allows any single noncharter county judicial circuit to collect a court surcharge to be used towards the maintenance and construction of judicial facilities Informal Calendar S Bills for Perfection--SB 1012-Dixon
# Modifies admissibility of chemical test results in intoxication related proceedings Informal Calendar S Bills for Perfection--SB 1014-Dixon
# Creates a lifetime permit to carry concealed firearms Informal Calendar S Bills for Perfection--SB 1026-Schatz, with SCS
# Modifies provisions relating to ratemaking for public utilities Informal Calendar S Bills for Perfection--SB 1028-Silvey, et al, with SCS
# Designates "Old Drum" as the historical dog of the state of Missouri, and designates "Jim the Wonder Dog" as Missouri's Wonder Dog Informal Calendar S Bills for Perfection--SB 1033-Pearce
# Establishes the third Monday of June as Ride to Work Day in Missouri H Calendar Senate Concurrent Resolutions for Third Reading
# Allows the Kansas City Police Department chief of police to appoint a lieutenant colonel to be responsible for homeland security matters Informal Calendar S Bills for Perfection--SB 1066-Curls
# Modifies certificate of need requirements for long-term care facilities Formal Calendar S Bills for Perfection--SB 1076-Parson, with SCS
# Modifies provisions relating to the ABLE act Informal Calendar S Bills for Perfection--SB 1074-Schmitt, with SCS
# Creates the Silver Alert System to aid in identifying and locating a missing endangered person Informal Calendar S Bills for Perfection--SB 1075-Wallingford
# Requires the governing board of each public institution of higher education to enter into a memorandum of understanding concerning sexual assault, domestic violence, dating violence, and stalking involving students on and off campus Informal Calendar S Bills for Perfection--SB 1085-Pearce
# Creates a property tax exemption for trails operated through railroad easements Informal Calendar S Bills for Perfection--SB 1094-Kehoe, with SCS
# Provides that a person who is injured by a product has 10 years after the sale or lease of the product to bring a suit for damages Informal Calendar S Bills for Perfection--SB 1091-Riddle
# Modifies provisions pertaining to non-participating manufacturers in the Master Settlement Agreement Informal Calendar S Bills for Perfection--SB 1096-Dixon and Keaveny, with SS (pending)
# Modifies provisions of law relating to MO HealthNet managed care Formal Calendar S Bills for Perfection--SB 1111-Brown
# Expresses support for the practice of Falun Dafa, also known as Falun Gong Resolutions Calendar - Reported from Committee--SCR 68-Schupp
# Designates the John Jordan 'Buck' O'Neil Memorial Bridge H Calendar Senate Bills for Third Reading
# Modifies provisions relating to multipurpose water resources Informal Calendar S Bills for Perfection--SB 1120-Hegeman, et al
# Provides licensing and taxation for daily fantasy sports games Informal Calendar S Bills for Perfection--SB 1131-Sifton
# Modifies the process for promulgation of an emergency rule by a state agency Informal Calendar S Bills for Perfection--SB 1144-Brown
# Modifies provisions relating to residential dwelling rentals Informal Calendar S Bills for Perfection--SB 1117-Wasson, with SCS
# Urges the United States Air Force to support basing and operating aircraft at Whiteman Air Force Base Resolutions Calendar - Reported from Committee--SR 2062-Pearce
# Establishes the Senate Committee on Utility Regulation and Infrastructure Investment Resolutions Calendar - Reported from Committee--SR 2196-Emery, with SCS
# Establishes the Senate Interim Committee on MO HealthNet Pharmacy Benefits Resolutions Calendar - Reported from Committee--SR 2215-Sater
# Establishes the Senate Interim Committee on Long-Term Care Facilities Resolutions Calendar - Reported from Committee--SR 2216-Cunningham, with SCS
# Establishes the Supporting and Strengthening Families Act relating to guardianships and guidelines for foster child caregivers, foster child involvement in case plans, and permanency hearings and modifies provisions regarding foster home placement HCS Reported Do Pass H Select Committee on Social Services (Pursuant to H Rule 27.12)
# Requires elder abuse investigators to provide specified written materials to alleged perpetrators HCS Reported Do Pass H Select Committee on Social Services (Pursuant to H Rule 27.12)
# Reauthorizes a tuition grant program for spouses and children of war vetarans Reported Do Pass H Select Committee on Social Services (Pursuant to H Rule 27.12)
# Harry Truman's 132nd birthday Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies provisions relating to political subdivisions Defeated on H Third Reading
# Modifies the definition of "current operating expenditures" and "state adequacy target" for the purposes of state funding and applies the definition of "average daily attendance" to charter schools Legislature voted to override Governor's veto
# Modifies the law relating to the offense of illegal reentry Referred H Select Committee on General Laws (Pursuant to H Rule 27.7)
# Modifies the membership composition and terms of service of the commissioners on the Conservation Commission Hearing Conducted H Government Oversight and Accountability
# Authorizes the conveyance of certain state properties Referred H Select Committee on Judiciary (Pursuant to H Rule 27.9)
# Disapproves and suspends the final order of rulemaking for the proposed rule 19 CSR 15-8.410 Personal Care Attendant Wage Range Legislature voted to override Governor's veto
# Creates procedures for higher education entity participation in Missouri Consolidated Health Care Plan Voted Do Pass S Veterans' Affairs and Health Committee
# Creates the "University of Missouri System Review Commission" H adopted
# Condemns California's anti-trade actions relating to eggs, calls on the California legislature to repeal AB 1437, and urges the voters of California to reconsider and repeal Proposition 2 Referred H Select Committee on Agriculture (Pursuant to H Rule 27.2)
# Commemorates May 1, 2016, as Law Day Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies the per barrel fee for the inspection of certain motor fuels Referred H Agriculture Policy
# Creates a tax credit for certain organizations working with ex-offenders SCS Voted Do Pass S Jobs, Economic Development and Local Government Committee (6683S.04C)
# Modifies provisions relating to procedures in criminal proceedings SCS Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee (6320S.02C)
# Prohibits the state from imposing penalties on individuals and religious entities who refuse to participate in same sex marriage ceremonies due to sincerely held religious beliefs Reported Do Not Pass H Emerging Issues
# Allows certain offenses to be prosecuted in the county in which the victim resides or conducts business or where stolen property was located Hearing Conducted H Civil and Criminal Proceedings
# Modifies provisions relating to the Missouri Works Program and the United States Department of Defense HCS Voted Do Pass H Select Committee on Commerce (Pursuant to H Rule 27.4)
# Defines "motorcycle profiling" and creates regulations to eliminate motorcycle profiling Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Establishes a new nursing licensure compact Hearing Conducted H Professional Registration and Licensing
# Allows for a connected vehicle technology testing program SCS Voted Do Pass S Transportation, Infrastructure and Public Safety Committee (5867S.02C)
# Modifies provisions regarding when a court must instruct the jury on an included criminal offense Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Authorizes legal counsel for the Department of Mental Health to have standing in certain hearings involving a person unable to stand trial due to lack of mental fitness Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Provides for supplemental reimbursement for emergency ground medical transportation services under MO HealthNet Voted Do Pass S Veterans' Affairs and Health Committee
# Increases the penalty when a county officer fails to return revised laws received by such officer to the clerk of the circuit court Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Establishes a Prescription Drug Monitoring Act Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Creates the "Capitol Complex Tax Credit Act" Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Modifies the law relating to prevailing wage Voted Do Pass S Small Business, Insurance and Industry Committee
# Requires children under the age of 18 to be prosecuted for most criminal offenses in juvenile courts unless the child is certified as an adult Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Enacts new provisions of law relating to professional employer organizations SCS Voted Do Pass S Small Business, Insurance and Industry Committee (5583S.04C)
# Creates a tax deduction for employee stock ownership plans Referred H Ways and Means
# Creates a right to unpaid leave for employees that are affected by domestic violence SCS Voted Do Pass S Small Business, Insurance and Industry Committee (5026S.02C)
# Establishes the Senior Services Growth and Development Program SCS Voted Do Pass S Seniors, Families and Children Committee (6415S.04C)
# Creates the Missouri State Board of Roofers which shall issue voluntary licenses to roofing contractors SCS Voted Do Pass S Financial and Governmental Organizations and Elections Committee (4151S.06C)
# Recognizes the 273rd anniversary of Thomas Jefferson's birth Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies provisions relating to hemp extract Voted Do Pass S Veterans' Affairs and Health Committee
# Provides that a landlord must keep security deposits in a depository institution and changes the amount a tenant can recover when the security deposit is wrongfully withheld SCS Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee (4426S.02C)
# Authorizes an earned income tax credit Voted Do Pass S Ways and Means Committee
# Modifies provisions of the Sunshine Law, including the mobile video recordings from law enforcement vehicles and body cameras Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Issues a summons to Mary Kogut of Planned Parenthood to appear before the Senate S adopted
# Issues a summons to Dr. James Miller of Pathology Services to appear before the Senate S adopted
# Allows the concealed carry of firearms on public transportation systems and the transporting of non-functioning or unloaded firearms on public buses Voted Do Pass S Transportation, Infrastructure and Public Safety Committee
# Requires the Department of Public Safety to establish a pilot program in St. Louis City to address the violent crime rate Voted Do Pass S Transportation, Infrastructure and Public Safety Committee
# Creates additional requirements for tow truck businesses and penalties for tow trucks responding to accidents in violation of the provisions of the act SCS Voted Do Pass S Transportation, Infrastructure and Public Safety Committee (6395S.02C)
# Modifies provisions relating to commercial driver's licenses SCS Voted Do Pass S Transportation, Infrastructure and Public Safety Committee (6571S.04C)
# 21st Century Leadership Academy Use of Chamber S Adopted
# Modifies provisions related to extended service warranties Voted Do Pass S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies procedures in guardianship and conservator proceedings for incapacitated or disabled persons Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies the law relating to orders issued by juvenile courts Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Requires the court to enter written findings of fact and conclusions of law for matters pertaining to child support and child custody Hearing Conducted S Seniors, Families and Children Committee
# Requires health carriers or managed care plans to offer medication synchronization services Voted Do Pass S Veterans' Affairs and Health Committee
# Requires a student athlete who is suspected of sustaining a concussion or brain injury be removed from competition and administered a side line test designed with a concussion protocol Bill Combined (w/SCS SBs 1050 & 940)
# Modifies requirements relating to brain injuries sustained by student athletes SCS Voted Do Pass (w/SCS SBs 1050 & 940) Veterans' Affairs and Health Committee (6471S.02C)
# Prohibits enforcement of any contractual provision that prevents disclosure of the contractual payment amount for health care services Hearing Conducted H Health and Mental Health Policy
# Allows a court to place a person on electronic monitoring with victim notification if a person has been charged with, or found guilty of, violating an order of protection Voted Do Pass S Transportation, Infrastructure and Public Safety Committee
# Modifies provisions relating to corporate security advisors SCS Voted Do Pass S Transportation, Infrastructure and Public Safety Committee (5201S.04C)
# Changes the "Farm-to-School Act" and program to the "Farm-to-Table Act" and program Bill Combined w/(SCS/SBs 1010, 878, & 958)
# Changes the "Farm-to-School Act" and program to the "Farm-to-Table Act" and program Bill Combined w/(SCS/SBs 1010, 878, & 958)
# Restricts the storage and use as evidence of data collected through automated license plate reader systems by government entities SCS Voted Do Pass S Transportation, Infrastructure and Public Safety Committee (6386S.02C)
# Prohibits disclosure of certain crime scene photographs and video recordings except under certain circumstances Voted Do Pass S Transportation, Infrastructure and Public Safety Committee
# Modifies provisions requiring LLC's owning rental or unoccupied property in Kansas City to list a property manager with the city clerk Hearing Conducted S Small Business, Insurance and Industry Committee
# Modifies provisions relating to event tickets SCS Voted Do Pass S Commerce, Consumer Protection, Energy and the Environment Committee (4603S.05C)
# Creates a regulatory system for self-service storage insurance and the selling of such insurance SCS Voted Do Pass S Small Business, Insurance and Industry Committee (5524S.02C)
# Designates October as Domestic Violence Awareness Month Hearing Scheduled But Not Heard S Rules, Joint Rules, Resolutions and Ethics Committee
# Designates May as Mental Health Awareness Month Hearing Scheduled But Not Heard S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies the law relating to discharge of employees under workers' compensation statutes Voted Do Pass S Small Business, Insurance and Industry Committee
# Modifies the authority of municipalities to offer certain communications services Hearing Conducted S Commerce, Consumer Protection, Energy and the Environment Committee
# Creates the Office of Missing Persons Advocate Hearing Conducted S Seniors, Families and Children Committee
# Changes the employer contribution for the College and University Retirement Plan and requires employees to contribute to the plan Voted Do Pass S General Laws and Pensions Committee
# Modifies provisions relating to the Uniform Commercial Code Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies provisions of law relating to abuse of children less than a year old and child abuse and neglect training SCS Voted Do Pass S Seniors, Families and Children Committee (6628S.02C)
# Modifies provisions of law relating to custody of in vitro human embryos SCS Voted Do Pass S Seniors, Families and Children Committee (6717S.02C)
# Modifies provisions relating to athletic trainers Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Licenses persons performing radiologic imaging or administering radiation therapy and establishes the Missouri Radiologic Imaging and Radiation Therapy Board of Examiners Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Prohibits the sale or offering of powdered alcohol and creates a crime of illegal possession of powdered alcohol Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Allows qualified motorcycle operators to operate motorcycles and motortricycles without protective headgear under certain conditions Bill Combined (w/SCS SBs 851 & 694)
# Provides that change in population shall not remove a city, county or political subdivision from operation of a law Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Modifies the disbursement of taxes paid under protest Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Creates the National Popular Vote Act Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Adds an optional motorcycle registration surcharge of five dollars to be deposited in the motorcycle safety trust fund Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Adds stationary utility vehicles to list of vehicles requiring drivers of motor vehicles to proceed with caution upon approach Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Removes criminal penalties for certain acts of staff members in the Oversight Division of the Joint Committee on Legislative Research Hearing Cancelled S Governmental Accountability and Fiscal Oversight Committee
# Modifies the duties and functions of the Joint Committee on Legislative Research Voted Do Pass S Governmental Accountability and Fiscal Oversight Committee
# Requires the Department of Higher Education to create guidance regarding notice of public employee eligibility for public service loan forgiveness Voted Do Pass S Education Committee
# Adopts the Compact for a Balanced Budget Bill Combined (w/SCS SBs 662 & 587)
# Applies to Congress for the calling of an Article V convention of states to propose certain amendments to the United States Constitution which place limits on the federal government Bill Combined (w/SBS SBs 53 & 44)
# Urges the federal government to return certain lands to western states where such lands are located Hearing Conducted S Rules, Joint Rules, Resolutions and Ethics Committee
# Subject to appropriation, requires the Commission for the Deaf and Hard of Hearing to provide grants to certain organizations that provide services to deaf-blind children, adults, and service providers SCS Voted Do Pass S Seniors, Families and Children Committee (6481S.02C)
# Creates the Foster Care Bill of Rights SCS Voted Do Pass S Seniors, Families and Children Committee (6421S.03C)
# Modifies several provisions relating to foster care Hearing Conducted S Seniors, Families and Children Committee
# Restricts the use of cell site simulator devices SCS Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee (4749S.02C)
# Provides that a juvenile's attorney must have the right to be heard on a request that restraints not be used in juvenile court Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Prohibits the use of restraints on children under the age of 17 and pregnant and post-postpartum offenders during court proceedings except in certain circumstances Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Allows those licensed by the Department of Agriculture to grow and handle industrial hemp SCS Voted Do Pass S Agriculture, Food Production and Outdoor Resources Committee (4164S.02C)
# Requires the question of whether to recall the county executive to be submitted to voters in St. Louis County Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Creates economic subsidies for qualified gaseous biofuel producers Voted Do Pass S Agriculture, Food Production and Outdoor Resources Committee
# Allows Cedar County to establish, if approved by voters, a local sales tax for the purpose of funding libraries Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Modifies provisions relating to the compensation of county officers SCS Voted Do Pass S Jobs, Economic Development and Local Government Committee (5539S.04C)
# Allows cities, towns, or villages located in first or second class counties to consolidate if they meet certain conditions Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Creates the "Missouri Task Force on Workforce Competitiveness" Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Clarifies the definition of "required student fees" and requires that student-established fees expire no later than ten years after the effective date of the fee Hearing Conducted S Education Committee
# Modifies provisions relating to cancellation or nonrenewal for automobile and homeowner's insurance policies SCS Voted Do Pass S Small Business, Insurance and Industry Committee (6073S.02C)
# Modifies provisions of law relating to workers' compensation Hearing Conducted S Small Business, Insurance and Industry Committee
# Establishes the Missouri Child Protection Registry Hearing Conducted S Seniors, Families and Children Committee
# Modifies several provisions relating to the Public School Retirement System of St. Louis Hearing Conducted S General Laws and Pensions Committee
# Allows retired members of MOSERS and MPERS who are rehired and reimburse the system for benefits received to recalculate credible service Hearing Conducted S General Laws and Pensions Committee
# Allows the board of trustees of the Public School Retirement System of the City of St. Louis to provide cost-of-living increases Hearing Conducted S General Laws and Pensions Committee
# Adds an exemption from the prohibition of physician referrals for physical therapy services to entities with whom the physician has a financial relationship Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Modifies provisions of law relating to filing for elections in certain charter counties SCS Voted Do Pass S Financial and Governmental Organizations and Elections Committee (6351S.03C)
# Prohibits discrimination between certain types of mental health professionals Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Floyd Riddick Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Creates the Missouri Qualified Solid Biomass Fuel Producer Incentive Fund to provide economic subsidies to solid biomass fuel producers SCS Voted Do Pass S Ways and Means Committee (6313S.04C)
# Modifies existing law to limit the MO HealthNet Division's recovery from a third-party to medical expenses Hearing Cancelled S Veterans' Affairs and Health Committee
# Modifies state law relating to stroke center designations and the collection of hospital emergency care data Hearing Cancelled S Veterans' Affairs and Health Committee
# Extends the sunset on certain healthcare provider reimbursement allowance taxes Hearing Conducted S Ways and Means Committee
# Requires the State Board of Education to assign classification designations to individual attendance centers Hearing Cancelled S Education Committee
# Establishes the "Student Online Personal Protection Act" Hearing Scheduled But Not Heard S Education Committee
# Modifies provisions relating to certain degree programs at certain higher education institutions Hearing Conducted S Education Committee
# Changes the age of mandatory retirement to sixty-five for uniformed members of the highway patrol Hearing Cancelled S General Laws and Pensions Committee
# Modifies provisions relating to covered prescription benefits SCS Voted Do Pass S Financial and Governmental Organizations and Elections Committee (5629S.02C)
# Modifies provisions of law relating to voting machines for persons who are blind or visually-impaired Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Removes a property tax exemption for real property belonging to the Missouri Department of Natural Resources Voted Do Pass S Ways and Means Committee
# Creates a state sales and use tax exemption for utilities, equipment, and materials used to generate or transmit electricity Voted Do Pass S Ways and Means Committee
# Imposes a tax on unauthorized, controlled substances Hearing Conducted S Ways and Means Committee
# Modifies titles that may be issued for motor vehicles previously issued a junking certificate Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Repeals and reenacts provisions of law regarding county prosecutors that were declared unconstitutional based on a procedural defect in the enacting legislation Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies the composition of the University of Missouri Board of Curators by adding a voting student member Second Read and Referred S Education Committee
# Establishes an Early Learning Quality Assurance Report pilot program Second Read and Referred S Education Committee
# Prohibits any person from serving more than two 4-year terms as county executive in Jackson, St. Charles, St. Louis, and Jefferson Counties Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Modifies provisions of law relating to the average weekly wage of certain employees under workers' compensation laws Second Read and Referred S Small Business, Insurance and Industry Committee
# Requires long-term care facilities to assist employees and volunteers in obtaining an influenza vaccination each year Second Read and Referred S Veterans' Affairs and Health Committee
# Requires licensed chiropractors and physical therapists to be reimbursed for the provision of MO HealthNet services Second Read and Referred S Veterans' Affairs and Health Committee
# Modifies provisions relating to property assessments for energy efficiency improvements Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies provisions of law regarding claims against public higher education institutions covered by the State Legal Expense Fund Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Authorizes the use of various incentives to attract jobs from Kansas border counties into Missouri Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Allows for a patient's designation of a caregiver to provide care following discharge from a hospital or ambulatory surgical center Second Read and Referred S Veterans' Affairs and Health Committee
# Creates new provisions of law relating to financial disclosure under campaign finance laws Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Prohibits the use of eminent domain for certain electric transmission line projects Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Allows each school district may rely on technical course work and skills assessments developed for industry-recognized certificates and credentials when establishing career and technical education offerings Second Read and Referred S Education Committee
# Requires each public institution of higher education to report the institution's administrative costs as a percent of its operating budget Second Read and Referred S Education Committee
# Amends a provision of law relating to rights of a child when taken into custody by changing the pronouns to "he or she" and "him or her" Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies appeal procedures for cases originating with the Public Service Commission Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Creates new provisions of law relating to traditional installment loans Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Modifies and creates several tax credits related to agriculture Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Creates the Missouri Radon Awareness Act Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Delineates procedures a court must follow when assessing a claim that the government has enforced a law that limits a person's constitutional rights Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Creates new constitutional amendment relating to congressional term limits Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Creates a tax credit for charitable donations to Love INC Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Allows enrollment in a health benefit plan by a pregnant person under certain circumstances Second Read and Referred S Small Business, Insurance and Industry Committee
# Modifies provisions relating to governing boards for unaccredited school districts Second Read and Referred S Education Committee
# Allows aluminum smelting facilities to submit an application, or aluminum smelting facilities together with an electrical corporation to submit a contract, to the Public Service Commission for an aluminum smelter rate Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Creates the offense of unlawful transfer of weapons for a licensed firearms dealer to deliver a handgun to a purchaser without waiting at least 24 hours Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Creates the Rx Cares for Missouri Program Second Read and Referred S Veterans' Affairs and Health Committee
# Prevents taxation of certain telecommunication services Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies the distribution of St. Louis County sales taxes and authorizes a retail sales tax to fund county law enforcement Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Specifies Metropolitan Community College District of Kansas City is a qualifying educational institution for the purposes of updating tourist-oriented directional highway signs Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Specifies that royalty payments to a dental franchisor by a licensee of the Dental Board operating a franchised dental office is not unlawful Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Modifies motor vehicle franchise practices Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies language relating to the distribution of sales taxes in St. Louis County Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Requires the Department of Higher Education to create guidance regarding notice of public employee eligibility for public service loan forgiveness Second Read and Referred S Education Committee
# Abolishes township road districts Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Requires the Department of Higher Education to create guidance regarding notice of public employee eligibility for public service loan forgiveness Second Read and Referred S Education Committee
# Extends the expiration date of the Agricultural Product Utilization Contributor Tax Credit and the New Generation Cooperative Incentive Tax Credit from 2016 to 2022 Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Modifies provisions relating to children involved in trafficking and prostitution Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Requires the Department of Elementary and Secondary Education to report in the statewide longitudinal data system the percentage of students in each school district who have received all required immunizations Second Read and Referred S Education Committee
# Modifies control and maintenance of the supplementary state highway system Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Modifies provisions of law relating to funding for the public service commission and the office of public counsel Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Establishes a tax credit for providing certain low-income veterans with housing Hearing Cancelled S Jobs, Economic Development and Local Government Committee
# Requires higher education institutions to inform students and employees about affirmative consent to sexual activity Hearing Conducted S Education Committee
# Allows students enrolled in approved virtual institutions to participate in the Access Missouri Financial Assistance Program SCS Voted Do Pass S Education Committee (4901S.02C)
# Requires all tax credit programs created on or after August 28, 2016 to comply with the Tax Credit Accountability Act of 2004 Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Establishes the Missouri Empowerment Scholarship Accounts Program Hearing Conducted S Education Committee
# Increases the penalties for knowingly allowing a minor to drink or possess alcohol or failing to stop a minor from drinking or possessing alcohol SCS Voted Do Pass S Transportation, Infrastructure and Public Safety Committee (4491S.02C)
# Allows the Wine and Grape Tax Credit to be used for used equipment and caps the credit at one million dollars annually Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Modifies provisions relating to instruction in human sexuality and sexually transmitted infections Hearing Conducted S Education Committee
# Creates the "Show Me Rural Jobs Act" Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Modifies provisions relating to tax increment financing, emergency service providers, and board members of fire protection and ambulance districts SCS Voted Do Pass S Jobs, Economic Development and Local Government Committee (5470S.05C)
# Authorizes incentives for data storage centers Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Modifies the certification procedures for licensing boat manufacturers and boat dealers Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Urges the National Geospatial-Intelligence Agency to build a new facility in St. Louis City H adopted
# Modifies provisions relating to videoconferencing at hearings before the Board of Probation and Parole Voted Do Pass S Transportation, Infrastructure and Public Safety Committee
# Creates the Land Reclamation Legal Settlement Commission and Fund to implement primary restoration projects in southeast Missouri Voted Do Pass S Governmental Accountability and Fiscal Oversight Committee
# Modifies exemptions to duty to retreat when using force against another person Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Exempts fantasy sports from gambling laws Hearing Conducted S Progress and Development Committee
# Requires the Department of Natural Resources to submit a budget analysis to certain committees in the General Assembly Voted Do Pass S Governmental Accountability and Fiscal Oversight Committee
# Modifies provisions relating to racial profiling in policing Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Requires that an applicant for a navigator license must take an exam created by the Department of Insurance and submit to a criminal background check Hearing Conducted S Small Business, Insurance and Industry Committee
# Modifies provisions relating to hazardous waste SCS Voted Do Pass S Commerce, Consumer Protection, Energy and the Environment Committee (4730S.03C)
# Creates regulations for the process of identifying deceased insureds and payments of life insurance death benefits for policies issued after January 1, 2017 SCS Voted Do Pass S Small Business, Insurance and Industry Committee (5416S.02C)
# Requires certain employers to file Missouri income tax returns electronically Removed S Consent Calendar
# Establishes a pilot program allowing noncustodial parents to reduce the amount of state debt owed SCS Voted Do Pass S Seniors, Families and Children Committee (6068S.02C)
# Modifies provisions relating to racial profiling in policing Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Requires health insurers to make updates to their electronic and paper dental services provider materials available to plan members Hearing Conducted S Small Business, Insurance and Industry Committee
# Creates the Missouri Electrical Industry Licensing Board and licensure requirements for a statewide electrical contractor's license Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Modifies provisions relating to health information organizations Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Modifies provisions relating to county prosecuting attorneys Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies laws relating to public defenders Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Requires a person who has been found guilty of driving while intoxicated to complete a victim impact program approved by the court Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Adds an element to the crime of aggravated or first degree stalking Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies sentencing and supervision provisions for offenders of sex crimes against children Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies provisions relating to the Children's Division Voted Do Pass S Seniors, Families and Children Committee
# Establishes guidelines for foster child caregivers, foster child involvement in case plans, and permanency hearings SCS Voted Do Pass S Seniors, Families and Children Committee (6145S.02C)
# Missouri YMCA Youth in Government S adopted
# Silver Haired Legislature S adopted
# MO Youth Leadership Forum-Students with Disabilities S adopted
# Authorizes a retail sales tax in St. Louis County to fund county law enforcement Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Requires public colleges and universities to post certain course information on their Internet websites Hearing Conducted S Education Committee
# Modifies the retirement allowance calculation for members of the Public School Retirement System with thirty-one or more years of service Hearing Conducted S Education Committee
# Modifies provisions relating to tuition assistance for combat veterans Hearing Conducted S Education Committee
# Prohibits political subdivisions from requiring that pet shops sell only animals obtained from a pound, animal shelter, or contract kennel SCS Voted Do Pass S Agriculture, Food Production and Outdoor Resources Committee (6196S.03C)
# Modifies laws regarding arbitration agreements between employers and at-will employees SCS Voted Do Pass S Small Business, Insurance and Industry Committee (4745S.02C)
# Exempts marijuana from certain forfeiture provisions relating to controlled substances Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies provisions relating to records of minor victims of sexual offenses SCS Voted Do Pass S Seniors, Families and Children Committee (6070S.02C)
# Creates standards for predetermination of health care benefits requests and responses Hearing Conducted S Small Business, Insurance and Industry Committee
# Modifies the law relating to special elections Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Modifies the law relating to vacancies in the office of county commissioner Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Modifies provisions relating to vacancies in county-elected offices Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Modifies several provisions relating to student safety Second Read and Referred S Education Committee
# Allows certain municipal hospitals to invest 25% of their funds in investment funds Second Read and Referred S Veterans' Affairs and Health Committee
# Changes the amount of restitution paid to an individual wrongfully convicted Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies provisions required to be in nuisance abatement ordinances enacted by municipalities and counties Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Creates new provisions of law relating to leave from employment Second Read and Referred S Small Business, Insurance and Industry Committee
# Modifies requirements relating to the pursuance and acceptance of grants by public school districts Second Read and Referred S Education Committee
# Allows physician assistants to determine the necessity of physical or chemical restraint of a patient in a mental health facility or program Second Read and Referred S Veterans' Affairs and Health Committee
# Creates a voluntary replacement alternative program for children's vaccines which do not contain human DNA content Second Read and Referred S Veterans' Affairs and Health Committee
# Requires the Oversight Division of the Joint Committee on Legislative Research to perform an actuarial analysis on the provision of marital and family therapy services to MO HealthNet participants Second Read and Referred S Veterans' Affairs and Health Committee
# Requires the Department of Health and Senior Services to promulgate regulations for the construction and renovation of hospitals which include certain standards Second Read and Referred S Veterans' Affairs and Health Committee
# Requires that any standards developed by the State Board of Education for the purposes of determining a child's eligibility for special educational services shall allow the consideration of trauma as a result of experience in foster care Second Read and Referred S Education Committee
# Requires hospitals to offer a pneumococcal vaccine to all inpatients 65 or older prior to discharge Second Read and Referred S Veterans' Affairs and Health Committee
# Increases the amount of the personal income tax cut and the business income deduction in current law Hearing Conducted S Ways and Means Committee
# Amends the Constitution to limit general revenue appropriations and mandate state income tax rate reductions in certain situations Hearing Conducted S Ways and Means Committee
# Divides the Thirty-Eighth Judicial Circuit and creates a new Forty-Sixth Judicial Circuit Signed by Governor
# Allows structured family caregiving as a covered service under MO HealthNet Hearing Conducted S Veterans' Affairs and Health Committee
# Creates the MO HealthNet Buy-In for Workers with Disabilities program Hearing Conducted S Veterans' Affairs and Health Committee
# Provides a tax deduction for income earned out of state Hearing Cancelled S Ways and Means Committee
# Creates a new constitutional provision relating parental rights Second Read and Referred S Seniors, Families and Children Committee
# Provides that the Citizens' Commission on Compensation for Elected Officials shall set the compensation for certain elected officials at a specific dollar amount Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies the Access Missouri Financial Assistance Program by adding eligibility requirements Bill Combined (w/SCS SBs 857 & 712)
# Prohibits the effectiveness of any federal regulation not authorized by federal law in the state of Missouri unless authorized by the General Assembly SCS Voted Do Pass S Governmental Accountability and Fiscal Oversight Committee (4837S.02C)
# Modifies the definition of "current operating expenditures" for the purposes of state funding and applies the definition of "average daily attendance" to charter schools Bill Combined (w/SCS SBs 586 & 651)
# Prohibits political subdivisions from enacting ordinances relating to the labeling or use of fertilizers or soil conditioners Voted Do Pass S Agriculture, Food Production and Outdoor Resources Committee
# Requires the reporting of lost or stolen firearms Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Requires law enforcement agencies in certain cities to require their officers to wear a camera while on duty and in uniform and record all contacts with people Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Modifies provisions regarding county law enforcement restitution funds Voted Do Pass S Jobs, Economic Development and Local Government Committee
# Modifies privacy protections for certain agricultural entities Voted Do Pass S Agriculture, Food Production and Outdoor Resources Committee
# Requires the Director of the Department of Natural Resources to sell at public auction property located in Oregon County by December 31, 2016 SCS Voted Do Pass S Governmental Accountability and Fiscal Oversight Committee (6226S.03C)
# Specifies that courts must order an evaluation by the Division of Youth Services to determine whether dual jurisdiction is appropriate for certain juvenile offenders Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies the provisions of law relating to campaign finance Hearing Conducted S Rules, Joint Rules, Resolutions and Ethics Committee
# Prohibits two-way telecommunications devices and their component parts in correctional centers and jails Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Removes the statute of limitations on civil actions and prosecutions involving offenses against children Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies the crime of animal trespass Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Allows the presiding judge of certain circuits to appoint a circuit court marshal Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Requires the Attorney General to screen prison volunteers for terrorist proclivities and the Corrections Department to report on procedures to reduce radicalization Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies the state's requirements to reimburse counties for certain costs related to imprisonment and electronic monitoring for criminal offenders Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Allows the Department of Revenue to issue REAL ID compliant driver's licenses and identification cards Hearing Conducted S General Laws and Pensions Committee
# Creates the offense of terrorism Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Changes the effective date of the repeal and enactment of certain provisions of the Uniform Interstate Family Support Act Bill Combined (w/SCS SBs 905 & 992)
# Relating to ride to work day in Missouri Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies provisions relating to election challengers Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Reauthorizes the Missouri Homestead Preservation tax credit program Voted Do Pass S Ways and Means Committee
# Provides that a managed care plan's network is adequate if the health carrier is accredited by the Accreditation for Ambulatory Health Care Hearing Conducted S Veterans' Affairs and Health Committee
# Allows Greene County, or any city within the county, to impose a sales tax, upon voter approval, to fund early childhood education Hearing Conducted S Ways and Means Committee
# Creates a tax deduction for dentists providing services to MO HealthNet participants Voted Do Pass S Ways and Means Committee
# Makes it a class B felony to physically take property from a person when the property is owned by a financial institution Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Applies ban on using cell phones related to text messaging while driving to all drivers Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Applies ban on using cell phones related to text messaging while driving to all drivers Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Requires the Department of Corrections to offer certain educational and job training programs to inmates Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Creates a tax credit for donations to an endowment fund of a community foundation Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Provides a process for the Parole Board to review the case histories of offenders serving more than 15 years in prison and recommend clemency or allow release on parole Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Requires every individual who is seventeen years or older and is arrested for a felony offense to provide a biological sample for DNA profiling Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Requires the driver and all passengers in a car or truck to wear a safety belt with certain exceptions Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Allows certain people to enter abandoned property to secure it, remove trash and graffiti, and maintain the grounds, and provides immunity from civil and criminal liability Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies provisions of law relating to products liability claims Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Creates the "Missouri Task Force on Fair, Nondiscriminatory Local Taxation Concerning Motor Vehicles, Trailers, Boats, and Outboard Motors" SCS Voted Do Pass S Governmental Accountability and Fiscal Oversight Committee (5747S.03C)
# Adds entering or remaining on a privately owned structure attached to another person's building or property to the list of actions that constitute first degree trespass Voted Do Pass S Judiciary and Civil and Criminal Jurisprudence Committee
# Enacts multiple provisions to protect the privacy of student data Hearing Conducted S Education Committee
# Requires the State Auditor to audit the University of Missouri System at least once annually Voted Do Pass S Governmental Accountability and Fiscal Oversight Committee
# Modifies provisions of law relating to construction management Bill Combined (w/SCS SBs 789 & 595)
# Provides that a nonpartisan judicial commission shall submit to the Governor a list of names, rather than a list of three names, to fill a judicial vacancy in a court under the nonpartisan court plan Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies Supreme Court Rule 55.03 regarding sanctions against lawyers, law firms, or parties for certain conduct Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies the definition of "customer-generator" in the Net Metering and Easy Connection Act Hearing Conducted S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies provisions relating to ratemaking for gas corporations Hearing Conducted S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies provisions regarding the administration of small probate estates Hearing Cancelled S Judiciary and Civil and Criminal Jurisprudence Committee
# Modifies provisions relating to trust protectors Hearing Cancelled S Judiciary and Civil and Criminal Jurisprudence Committee
# Requires law enforcement agencies to develop certain policies for eyewitness identification procedures Hearing Conducted S Judiciary and Civil and Criminal Jurisprudence Committee
# Urges Maryland Heights City Council to not provide tax incentives for certain developments Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies class one election offenses Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Modifies the statute specifying when police officers are justified in using deadly force Bill Combined (w/SCS/SBs 661, 726 & 741)
# Expands the crimes eligible for expungement and modifies the time period a person must wait before being eligible to petition for expungement Bill Combined (w/SCS/SBs 588, 603 & 942)
# Modifies bond requirements for certain county offices Hearing Conducted S Financial and Governmental Organizations and Elections Committee
# Modifies the statute specifying when police officers are justified in using deadly force Bill Combined (w/SCS/SBs 661, 726 & 741)
# Modifies provisions relating to the election of political parties SCS Voted Do Pass S Financial and Governmental Organizations and Elections Committee (4481S.02C)
# Modifies provisions relating to the expungement of criminal records Bill Combined (w/SCS/SBs 588, 603 & 942)
# Creates regulations for transportation network companies Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Allows a charter county to submit to voters a proposal for a $5 user fee on instruments recorded with the Recorder of Deeds for an assistance program for homeless persons Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Prohibits the use of certain events in determination of insurance policy rates and issuance Second Read and Referred S Small Business, Insurance and Industry Committee
# Expands the prohibition on the use of hand-held communications devices while operating a motor vehicle Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Requires Department of Labor to establish a state OSHA plan to submit to the United States Department of Labor Second Read and Referred S Small Business, Insurance and Industry Committee
# Adds ambulance districts to the types of political subdivisions whose funds must be secured by the deposit of a certain type of security Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Authorizes deductions for small business employing certain employees Second Read and Referred S Small Business, Insurance and Industry Committee
# Expands the requirement for children to wear personal flotation devices Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Bars discrimination based on sexual orientation or gender identity Voted Do Pass S Progress and Development Committee
# Prohibits quasi-governmental entities from entering into long-term bond agreements that financially obligate the state Voted Do Pass S Governmental Accountability and Fiscal Oversight Committee
# Requires the Director of the Department of Natural Resources to give preference to Missouri residents or businesses whose primary place of business is located in Missouri when awarding state park public concessions contracts Hearing Scheduled But Not Heard S Agriculture, Food Production and Outdoor Resources Committee
# Establishes the Consumer Legal Funding Model Act Hearing Conducted S Progress and Development Committee
# Modifies provisions related to watercraft registration Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Specifies that the state is not liable for, and shall not pay, the debts of financially insolvent municipalities Hearing Conducted S Governmental Accountability and Fiscal Oversight Committee
# Repeals the law pertaining to prevailing wage Hearing Conducted S Small Business, Insurance and Industry Committee
# Modifies the law relating to unlawful discrimination Hearing Conducted S Small Business, Insurance and Industry Committee
# Requires long-term care facilities to institute policies facilitating familial involvement in the well-being and support of its residents Voted Do Pass S Seniors, Families and Children Committee
# Amends the Constitution to restrict stadium funding Hearing Scheduled But Not Heard S General Laws and Pensions Committee
# Establishes the Joint Committee on Public Assistance Bill Combined w/(SCS/SBs 688 & 854)
# Institutes a gift ban for the members of the General Assembly and their candidate committees Hearing Conducted S Rules, Joint Rules, Resolutions and Ethics Committee
# Allows emergency workers to request, receive and submit absentee ballots Voted Do Pass S Financial and Governmental Organizations and Elections Committee
# Modifies laws regarding the renewal of licenses issued by the Board of Pharmacy Bill Combined (w/SCS SB's 865 & 866)
# Modifies provisions of law relating to ethics SCS Voted Do Pass S Rules, Joint Rules, Resolutions and Ethics Committee (4624S.08C)
# Modifies certificate of need requirements for long-term care facilities Hearing Scheduled But Not Heard S Veterans' Affairs and Health Committee
# Disapproves the regulation filed by the State Tax Commission on December 29, 2015, that establishes new values for certain agricultural and horticultural property Referred H Agriculture Policy
# Creates a tax credit for charitable contributions Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Requires certain policies on police-worn cameras, allows for the collection of a court fee and creates a fund for the cameras, and makes data from the cameras closed records Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Modifies provisions relating to employee wages Second Read and Referred S Small Business, Insurance and Industry Committee
# Modifies provisions for the abatement of vacant nuisance properties in Kansas City Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Modifies the minimum wage laws Second Read and Referred S Small Business, Insurance and Industry Committee
# Requires the legislature to appropriate all funds to which public school districts are entitled under the funding formula established by law Second Read and Referred S Appropriations Committee
# Provides for the expansion of MO HealthNet services beginning January 1, 2017 Second Read and Referred S Veterans' Affairs and Health Committee
# Modifies provisions of law relating to the minimum wage Second Read and Referred S Small Business, Insurance and Industry Committee
# Establishes provisions relating to workers' compensation large deductible policies Second Read and Referred S Small Business, Insurance and Industry Committee
# Limits the enactment of general laws to the first legislative session of a General Assembly, except for certain emergency legislation Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Authorizes tax credits for earnings taxes for individuals who live and work in different states Second Read and Referred S Ways and Means Committee
# Requires the Department of Higher Education to develop and maintain website containing certain information on institutions of higher education Second Read and Referred S Education Committee
# Modifies provisions related to health insurance discrimination Second Read and Referred S Small Business, Insurance and Industry Committee
# Establishes the number, classification and rates of pay for Senate employees S adopted
# Creates new provisions of law relating to leave from employment Second Read and Referred S Seniors, Families and Children Committee
# Modifies the law relating to administrative leave for public employees Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Removes a sectional reference to a section of law that was repealed in 2012 relating to the closing times of retailers selling intoxicating liquor Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Allows students to enroll in a school district other than his or her school district of residence or in a charter school for the purpose of attending virtual courses or programs Second Read and Referred S Education Committee
# Removes the current ban on carrying concealed firearms in higher education institutions Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Modifies the composition of the Career and Technical Education Advisory Council Bill Combined (w/SCS SBs 620 & 582)
# Removes the current ban on carrying concealed firearms in higher education institutions, but allows institutions to ban concealed firearms under certain conditions Hearing Conducted S Transportation, Infrastructure and Public Safety Committee
# Provides that licensed liquor retailers may use dispensing systems that allow patrons to self-dispense up to 16 ounces of wine Hearing Conducted S Jobs, Economic Development and Local Government Committee
# Modifies provisions relating to employee wages Hearing Conducted S Small Business, Insurance and Industry Committee
# Prohibits planned communities from barring the installation of solar energy systems Hearing Conducted S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies provisions related to health insurance Hearing Conducted S Small Business, Insurance and Industry Committee
# Modifies provisions of law as it relates to voter photo identification Voted Do Pass S Financial and Governmental Organizations and Elections Committee
# Modifies the law relating to voting procedures SCS Voted Do Pass S Financial and Governmental Organizations and Elections Committee (4089S.03C)
# Modifies certificate of need requirements for long-term care facilities Hearing Cancelled S Veterans' Affairs and Health Committee
# Disapproves the regulation filed by the State Tax Commission on December 29, 2015, that establishes new values for certain agricultural and horticultural property Bill Combined (w/SCS SCRs 51 & 52)
# Allows Kansas City to employ airport police officers Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Adds sheltered workshop boards to the definition of "political subdivision" for purposes of laws allowing political subdivisions to cooperate with public and private entities Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Creates a regulatory scheme for homeowners' associations Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies the civil penalty for violating certain underground facility safety standards Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Allows the creation and issuance of insurance policies covering earthquake loss under the Missouri FAIR Plan Second Read and Referred S Small Business, Insurance and Industry Committee
# Ratifies the Equal Rights Amendment to the United States Constitution Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies the civil penalty for violating federally mandated natural gas safety standards Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Requires an insurer to send an insured written notification of policy renewal Second Read and Referred S Small Business, Insurance and Industry Committee
# Requires schools and school district to provide home school students the opportunity to participate in extracurricular activities Second Read and Referred S Education Committee
# Modifies provisions of law relating to project labor agreements Second Read and Referred S Small Business, Insurance and Industry Committee
# Requires St. Louis City and St. Louis County to increase the number of contracts awarded to women's and minority business enterprises Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Modifies provisions related to University of Missouri extension councils Second Read and Referred S Education Committee
# Requires certain employees of the Department of Corrections to receive hazardous duty pay Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Requires hospitals and ambulatory surgical centers to report prices for most common procedures Second Read and Referred S Veterans' Affairs and Health Committee
# Allows for the use of medical marijuana to treat serious conditions Second Read and Referred S Veterans' Affairs and Health Committee
# Increases the penalties and driver license suspension periods for those who fail to yield the right-of-way in certain instances Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Repeals the exception to the duty of scrap metal operators to obtain certificates of title for certain inoperable motor vehicles Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies provisions of law relating to the right of suffrage for former felons Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Transfers money from certain funds administered by the Department of Natural Resources to general revenue Hearing Conducted S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies provisions relating to feral hogs Hearing Conducted S Agriculture, Food Production and Outdoor Resources Committee
# Expands the authority of the Governor to convey easements without the approval of the General Assembly and expands the rights granted by the easements Hearing Conducted S Governmental Accountability and Fiscal Oversight Committee
# Use of Chamber/Missouri Catholic Conference S adopted
# Use of Chamber/Missouri Girls State S adopted
# Changes the date for final passage of bills in a regular session of the General Assembly Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies provisions regarding professional nursing and collaborative practice arrangements Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Modifies the number of members of the General Assembly and limits service in the General Assembly to sixteen years in any proportion between the House and Senate Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies the law relating to ethics reform Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Allows pharmacists and pharmacy technicians to sell and dispense opioid antagonists Second Read and Referred S Veterans' Affairs and Health Committee
# Repeals an incorrect intersectional reference in regard to regional recreational districts Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Creates a right to access medical marijuana Second Read and Referred S Veterans' Affairs and Health Committee
# Creates a regulatory system for self-service storage insurance and the selling of such insurance Second Read and Referred S Small Business, Insurance and Industry Committee
# Establishes legislative procedures for regulating previously unregulated professions Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Modifies certain constitutional amendments relating to members of the General Assembly Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies the laws relating to disclosure requirements to the Ethics Commission Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Requires each public school to screen each student for dyslexia and related disorders Second Read and Referred S Education Committee
# Modifies cost-sharing requirements for health benefit plans offered by health maintenance organizations Second Read and Referred S Small Business, Insurance and Industry Committee
# Repeals provisions of law requiring the licensing and taxation of peddlers by counties Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Creates new sections of law relating to leave from employment Second Read and Referred S Small Business, Insurance and Industry Committee
# Modifies certificate of need requirements for long-term care facilities Second Read and Referred S General Laws and Pensions Committee
# Creates the Energy Efficiency Competitive Resource Acquisition Act Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Provides for the certification of euthanasia technicians Second Read and Referred S Agriculture, Food Production and Outdoor Resources Committee
# Modifies a section reference in provisions relating to municipal courts Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Requires employees and volunteers of specified public and private institutions to receive an influenza vaccination every year Second Read and Referred S Veterans' Affairs and Health Committee
# Creates new constitutional provisions relating to ethics Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Provides that attorneys and title insurance companies are not precluded by land surveyor statutes from preparing property descriptions Second Read and Referred S Small Business, Insurance and Industry Committee
# Requires the Missouri Department of Natural Resources to submit an initial state plan and 2-year extension to the Environmental Protection Agency by June 30, 2016 Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies provisions relating to business filing fees Second Read and Referred S Small Business, Insurance and Industry Committee
# Modifies provisions relating to child care facility licensure Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Modifies provisions of law relating to wages paid to employees Second Read and Referred S Small Business, Insurance and Industry Committee
# Modifies provisions relating to natural resource damages authorized to be recovered by the state natural resources trustee Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Enacts new sections of law relating to publicly-financed elections Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Modifies the law relating to elections Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Creates the Board of Administrative Appeals and provides that a person is entitled a hearing before the Board following a proceeding before a governmental agency Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Exempts certain motor vehicles older than ten years from the sales tax on titling Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Modifies residential property receivership Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Creates term limits for members of the State Board of Education Second Read and Referred S Education Committee
# Requires school districts to adopt antibullying policies Second Read and Referred S Education Committee
# Prohibits a workforce development agency from knowingly omitting from any bidding process an entity with whom it has a contract Second Read and Referred S Governmental Accountability and Fiscal Oversight Committee
# Restricts the Department of Elementary and Secondary Education from creating certain reports that include data of any children in facilities serving neglected children or delinquent children Second Read and Referred S Education Committee
# Prohibits employers from inquiring into or considering the criminal records of applicants before offering a conditional offer of employment Second Read and Referred S Small Business, Insurance and Industry Committee
# Creates the crimes of failing to stop illegal weapon possession, negligent storage of a weapon, and failure to notify a school of weapon ownership Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Modifies and enacts provisions relating to law enforcement officers Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Creates a crime for employers who divulge certain personal information of employees and customers Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Prohibits each house of the General Assembly from adoption of an amendment to a bill if certain conditions are not met Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# States the intent of the General Assembly and the people of this state to amend the U.S. Constitution to guarantee every citizen of this country the right to vote Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Requires the St. Louis City and Kansas City school districts to implement reading plans for struggling students prior to promotion to third grade Second Read and Referred S Education Committee
# Modifies several provisions relating to elementary and secondary education Second Read and Referred S Education Committee
# Allows a person to possess up to one ounce of marijuana and provides a licensure process for retail marijuana stores, cultivation facilities, and products manufacturers Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Creates the Missouri Teen Dating Violence Prevention Education Act to educate teens about dating and domestic violence Second Read and Referred S Education Committee
# Requires the Senate to try all impeachments except for the impeachment of the Governor, which shall be tried by the Chief Justice of the Missouri Supreme Court Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Specifies that Kansas City may require the registration of certain properties Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Modifies the law relating to collective bargaining representatives Second Read and Referred S Small Business, Insurance and Industry Committee
# Creates the crimes of failing to stop illegal firearm possession, negligent storage of a firearm, and failure to notify a school of firearm ownership Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Changes the amount of damages that a tenant can recover when the security deposit is wrongfully withheld by a landlord Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Provides a method for judicial consideration of whether race played a role in decisions to impose or seek the death penalty Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Creates a new tax credit for first time purchasers of homes in a blighted area that will be used for owner-occupancy Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Repeals provisions regarding nonjudicial foreclosure proceedings and requires all foreclosure proceedings to be handled judicially Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Changes the notice requirement to a tenant in a foreclosure action from ten days to ninety days Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Provides that defendants in tort actions shall only be held severally liable and not jointly Second Read and Referred S Small Business, Insurance and Industry Committee
# Requires all public school restrooms, locker rooms, and shower rooms be designated for and used by male or female students only Second Read and Referred S Education Committee
# Changes the maximum authorization on low-income housing project tax credits from $6 million to $12 million Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Modifies the requirements for school antibullying policies Second Read and Referred S Education Committee
# Modifies the law relating to labor organizations Second Read and Referred S Small Business, Insurance and Industry Committee
# Allows certain assistant physicians, advanced practice registered nurses, and physician assistants to prescribe all Schedule II medications Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Creates the Missouri Parent/Teacher Involvement Program to provide grant awards to schools to develop and build trusting relationships between families and school staff Second Read and Referred S Education Committee
# Requires electrical corporations to track costs for complying with the Clean Power Plan and itemize such costs on customer bills Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies several provisions relating to elementary and secondary education Second Read and Referred S Education Committee
# Modifies requirements for special road district commissioner elections Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Eliminates income taxes and replaces them with an expanded sales and use tax and creates a property tax relief credit Second Read and Referred S Ways and Means Committee
# Provides for the expansion of MO HealthNet services beginning January 1, 2017 Second Read and Referred S Veterans' Affairs and Health Committee
# Modifies the law relating to school start dates Second Read and Referred S Education Committee
# Modifies several provisions relating to elementary and secondary education Second Read and Referred S Education Committee
# Amends the Constitution to modify state highway maintenance by instituting a motor fuel tax and restoring certain state highways to local control Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Modifies the law relating to public labor organizations Second Read and Referred S Small Business, Insurance and Industry Committee
# Makes St. Louis city a part of St. Louis county Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Imposes a gift ban for the members of the General Assembly and their candidate committees Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Creates a limit for the total amount of tax credits that may be authorized in a fiscal year Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Requires a portion of sales and use taxes collected to be deposited into the State Road Fund Second Read and Referred S Transportation, Infrastructure and Public Safety Committee
# Eliminates a provision allowing for property tax levy adjustments for inflation and modifies standing for Hancock Amendment challenges Second Read and Referred S Ways and Means Committee
# Modifies the law relating to consumer credit interest rates Second Read and Referred S Financial and Governmental Organizations and Elections Committee
# Requires the State Auditor to make a one-time report on the costs of administering the death penalty Second Read and Referred S Governmental Accountability and Fiscal Oversight Committee
# Modifies provisions regarding the ability of neighborhood organizations to bring nuisance actions in certain cities and counties Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Modifies provisions relating to community solar gardens Second Read and Referred S Commerce, Consumer Protection, Energy and the Environment Committee
# Modifies the law relating to occupational diseases under workers' compensation Second Read and Referred S Small Business, Insurance and Industry Committee
# Modifies the Higher Education Academic Scholarship Program by expanding eligibility requirements and by adding the option of receiving forgivable loans Second Read and Referred S Education Committee
# Requires the Senate, beginning January 1, 2017, to try all impeachments except for the impeachment of the Governor, which shall be tried by the Chief Justice of the Missouri Supreme Court Second Read and Referred S Judiciary and Civil and Criminal Jurisprudence Committee
# Establishes the Missouri anti-corruption amendment Second Read and Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# Creates a tax credit for adoption of dogs or cats from a shelter Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Authorizes the creation of Show-me Small Business Districts Second Read and Referred S Jobs, Economic Development and Local Government Committee
# Modifies provisions relating to the employment of teachers in school districts Second Read and Referred S Education Committee
# Creates an instructional waiver review board for the University of Missouri System Second Read and Referred S Education Committee
# Proposed Rule Change - Rule 16 reallocates use of reporters' table in Senate Chamber S adopted, as amended
# Expresses the support of the General Assembly for debt-free higher education Referred S Rules, Joint Rules, Resolutions and Ethics Committee
# WITHDRAWN Bill Withdrawn
# WITHDRAWN Bill Withdrawn
