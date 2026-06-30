from django.core.management.base import BaseCommand
from core.models import TrafficRule, TrafficSign, SafetyTip, EmergencyContact


class Command(BaseCommand):
    help = "Populate the database with sample traffic rules, signs, safety tips, and emergency contacts."

    def handle(self, *args, **options):
        self.seed_traffic_rules()
        self.seed_traffic_signs()
        self.seed_safety_tips()
        self.seed_emergency_contacts()
        self.stdout.write(self.style.SUCCESS("Sample data has been loaded successfully."))

    def seed_traffic_rules(self):
        rules = [
            ("Wear a Helmet", "All two-wheeler riders and pillion passengers must wear an ISI-marked helmet at all times while riding.", "Fine of ₹1,000 and 3-month license suspension"),
            ("Seatbelt is Mandatory", "All occupants of a four-wheeler, including those in the back seat, must wear a seatbelt while the vehicle is in motion.", "Fine of ₹1,000"),
            ("No Mobile Phone While Driving", "Using a handheld mobile phone for calls or texting while driving is strictly prohibited.", "Fine of ₹1,000 to ₹5,000"),
            ("Obey Speed Limits", "Drivers must not exceed the posted speed limit for the road type and vehicle category.", "Fine of ₹1,000–₹2,000 depending on vehicle type"),
            ("No Drunk Driving", "Driving under the influence of alcohol or drugs is a serious offence.", "Fine up to ₹10,000 and/or imprisonment up to 6 months"),
            ("Stop at Red Lights", "Vehicles must come to a complete stop at red traffic signals and proceed only when the signal turns green.", "Fine of ₹1,000–₹5,000"),
            ("Maintain Lane Discipline", "Drivers must stay within marked lanes and signal clearly before changing lanes.", "Fine of ₹1,000"),
            ("Give Way to Pedestrians", "Vehicles must yield to pedestrians at zebra crossings and designated crossing points.", "Fine of ₹500–₹1,000"),
            ("No Overloading", "Vehicles must not carry passengers or cargo beyond their rated capacity.", "Fine of ₹2,000 plus ₹1,000 per extra passenger/ton"),
            ("Carry Valid Documents", "Drivers must carry a valid driving license, registration certificate, insurance, and pollution certificate at all times.", "Fine of ₹500–₹5,000 depending on the missing document"),
        ]
        for title, desc, penalty in rules:
            TrafficRule.objects.get_or_create(title=title, defaults={'description': desc, 'penalty': penalty})

    def seed_traffic_signs(self):
        signs = [
            ("Stop Sign", "mandatory", "An octagonal red sign indicating that drivers must come to a complete stop before proceeding."),
            ("No Entry", "mandatory", "A circular red sign with a white horizontal bar indicating vehicles are not allowed to enter."),
            ("Speed Limit", "mandatory", "A circular sign displaying the maximum speed permitted on that stretch of road."),
            ("Compulsory Turn Left/Right", "mandatory", "A round blue sign with an arrow indicating the only direction vehicles may turn."),
            ("No Parking", "mandatory", "A circular sign with a diagonal line over a 'P', indicating parking is not allowed."),
            ("Pedestrian Crossing", "cautionary", "A triangular sign warning drivers of a pedestrian crossing ahead."),
            ("School Ahead", "cautionary", "A triangular sign warning drivers to slow down near a school zone."),
            ("Sharp Curve Ahead", "cautionary", "A triangular sign warning of an upcoming sharp bend in the road."),
            ("Narrow Bridge", "cautionary", "A triangular sign warning that the road ahead narrows, typically at a bridge."),
            ("Slippery Road", "cautionary", "A triangular sign warning that the road surface may be slippery, especially in wet conditions."),
            ("Hospital", "informatory", "A rectangular blue sign indicating the direction or location of a nearby hospital."),
            ("Fuel Station", "informatory", "A rectangular blue sign indicating a nearby petrol/fuel station."),
            ("Parking Available", "informatory", "A rectangular blue sign indicating a designated parking area."),
            ("One Way", "informatory", "A rectangular sign indicating traffic may only travel in one direction on that road."),
        ]
        for name, cat, desc in signs:
            TrafficSign.objects.get_or_create(name=name, defaults={'category': cat, 'description': desc})

    def seed_safety_tips(self):
        tips = [
            ("Check Mirrors Before Changing Lanes", "driver", "Always check your side and rearview mirrors, and use indicators, before changing lanes or turning."),
            ("Maintain a Safe Following Distance", "driver", "Keep at least a 3-second gap from the vehicle ahead to allow time to react to sudden stops."),
            ("Never Drive While Fatigued", "driver", "Fatigue slows reaction time as much as alcohol. Take breaks on long drives and avoid driving late at night if drowsy."),
            ("Always Wear a Properly Fastened Helmet", "rider", "Make sure your helmet strap is fastened snugly — an unfastened helmet offers little protection in a fall."),
            ("Use Reflective Gear at Night", "rider", "Wear bright or reflective clothing when riding at night to remain visible to other vehicles."),
            ("Avoid Weaving Between Lanes", "rider", "Constant lane-weaving increases the risk of collision and reduces your visibility to other drivers."),
            ("Use Designated Crossings", "pedestrian", "Always cross at zebra crossings or designated pedestrian crossings, and look both ways before crossing."),
            ("Make Eye Contact with Drivers", "pedestrian", "Before crossing, try to make eye contact with approaching drivers to confirm they have seen you."),
            ("Avoid Using Phones While Crossing", "pedestrian", "Stay alert and avoid distractions like phones or headphones when crossing roads."),
            ("Wear a Helmet While Cycling", "cyclist", "A properly fitted helmet significantly reduces the risk of head injury in a cycling accident."),
            ("Use Hand Signals", "cyclist", "Signal your turns clearly with your hand so drivers and pedestrians can anticipate your movement."),
            ("Plan Your Route in Advance", "general", "Knowing your route ahead of time reduces last-minute lane changes and distracted navigation."),
            ("Keep Your Vehicle Well-Maintained", "general", "Regularly check brakes, tyres, lights, and wipers — mechanical failure is a preventable cause of accidents."),
        ]
        for title, audience, content in tips:
            SafetyTip.objects.get_or_create(title=title, defaults={'audience': audience, 'content': content})

    def seed_emergency_contacts(self):
        contacts = [
            ("National Police Helpline", "police", "100", "For any police emergency or to report a crime in progress.", "National (India)"),
            ("National Ambulance Service", "ambulance", "108", "For medical emergencies and ambulance dispatch.", "National (India)"),
            ("Fire Department", "fire", "101", "For fire emergencies and rescue operations.", "National (India)"),
            ("National Highways Helpline", "highway", "1033", "For accidents, breakdowns, or hazards on national highways.", "National (India)"),
            ("Women Helpline", "women", "1091", "24x7 helpline for women in distress or facing harassment.", "National (India)"),
            ("Unified Emergency Number", "other", "112", "Single emergency number covering police, fire, and medical services.", "National (India)"),
            ("Road Accident Emergency Service", "ambulance", "1073", "Dedicated helpline for road accident victims on national highways.", "National (India)"),
        ]
        for name, cat, phone, desc, region in contacts:
            EmergencyContact.objects.get_or_create(
                name=name, phone_number=phone,
                defaults={'category': cat, 'description': desc, 'region': region}
            )
