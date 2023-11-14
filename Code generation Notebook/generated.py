from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime


class ConfidentialityValueEnum1(Enum):
    INTERNAL_USE = "internalUse"
    NO_RESTRICTION = "noRestriction"
    RESTRICTED_TO_AUTHORITIES = "restrictedToAuthorities"
    RESTRICTED_TO_AUTHORITIES_AND_TRAFFIC_OPERATORS = "restrictedToAuthoritiesAndTrafficOperators"
    EXTENDED = "_extended"


class InformationDeliveryServicesEnum1(Enum):
    ANY_GENERAL_DELIVERY_SERVICE = "anyGeneralDeliveryService"
    SAFETY_SERVICES = "safetyServices"
    VMS = "vms"
    EXTENDED = "_extended"


class InformationStatusEnum1(Enum):
    REAL = "real"
    SECURITY_EXERCISE = "securityExercise"
    TECHNICAL_EXERCISE = "technicalExercise"
    TEST = "test"
    EXTENDED = "_extended"


@dataclass
class MultilingualStringValue:
    class Meta:
        target_namespace = "http://levelC/schema/3/common"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 1024,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Reference:
    class Meta:
        target_namespace = "http://levelC/schema/3/common"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class ValidityStatusEnum1(Enum):
    ACTIVE = "active"
    PLANNED = "planned"
    SUSPENDED = "suspended"
    DEFINED_BY_VALIDITY_TIME_SPEC = "definedByValidityTimeSpec"
    EXTENDED = "_extended"


@dataclass
class VersionedReference:
    class Meta:
        target_namespace = "http://levelC/schema/3/common"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ExtensionType:
    class Meta:
        name = "_ExtensionType"
        target_namespace = "http://levelC/schema/3/common"

    anyElement: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


class AccidentCauseEnum1(Enum):
    AVOIDANCE_OF_OBSTACLES = "avoidanceOfObstacles"
    DRIVER_DISTRACTION = "driverDistraction"
    DRIVER_DRUG_ABUSE = "driverDrugAbuse"
    DRIVER_ILLNESS = "driverIllness"
    EXCEEDING_SPEEDS_LIMITS = "exceedingSpeedsLimits"
    EXCESS_ALCOHOL = "excessAlcohol"
    EXCESSIVE_DRIVER_TIREDNESS = "excessiveDriverTiredness"
    IMPERMISSIBLE_MANOEUVRE = "impermissibleManoeuvre"
    LIMITED_VISIBILITY = "limitedVisibility"
    NOT_KEEPING_ASAFE_DISTANCE = "notKeepingASafeDistance"
    ON_THE_WRONG_SIDE_OF_THE_ROAD = "onTheWrongSideOfTheRoad"
    PEDESTRIAN_IN_ROAD = "pedestrianInRoad"
    POOR_LANE_ADHERENCE = "poorLaneAdherence"
    POOR_MERGE_ENTRY_OR_EXIT_JUDGEMENT = "poorMergeEntryOrExitJudgement"
    POOR_ROAD_SURFACE_CONDITION = "poorRoadSurfaceCondition"
    POOR_SURFACE_ADHERENCE = "poorSurfaceAdherence"
    UNDISCLOSED = "undisclosed"
    UNKNOWN = "unknown"
    VEHICLE_FAILURE = "vehicleFailure"
    OTHER = "other"
    EXTENDED = "_extended"


class AccidentTypeEnum1(Enum):
    ACCIDENT = "accident"
    ACCIDENT_INVOLVING_HAZARDOUS_MATERIALS = "accidentInvolvingHazardousMaterials"
    ACCIDENT_INVOLVING_HEAVY_LORRIES = "accidentInvolvingHeavyLorries"
    ACCIDENT_INVOLVING_MASS_TRANSIT_VEHICLE = "accidentInvolvingMassTransitVehicle"
    ACCIDENT_INVOLVING_PUBLIC_TRANSPORT = "accidentInvolvingPublicTransport"
    ACCIDENT_INVOLVING_RADIOACTIVE_MATERIAL = "accidentInvolvingRadioactiveMaterial"
    ACCIDENT_INVOLVING_TRAIN = "accidentInvolvingTrain"
    COLLISION = "collision"
    MULTIPLE_VEHICLE_ACCIDENT = "multipleVehicleAccident"
    SECONDARY_ACCIDENT = "secondaryAccident"
    SERIOUS_INJURY_OR_FATAL_ACCIDENT = "seriousInjuryOrFatalAccident"
    VEHICLE_STUCK_UNDER_BRIDGE = "vehicleStuckUnderBridge"
    OTHER = "other"
    EXTENDED = "_extended"


class CollisionTypeEnum1(Enum):
    COLLISION_WITH_ANIMAL = "collisionWithAnimal"
    COLLISION_WITH_OBSTACLE = "collisionWithObstacle"
    COLLISION_WITH_PERSON = "collisionWithPerson"
    HEAD_ON_COLLISION = "headOnCollision"
    HEAD_ON_OR_SIDE_COLLISION = "headOnOrSideCollision"
    MULTIPLE_VEHICLE_COLLISION = "multipleVehicleCollision"
    REAR_COLLISION = "rearCollision"
    SIDE_COLLISION = "sideCollision"
    EXTENDED = "_extended"


class ProbabilityOfOccurrenceEnum1(Enum):
    CERTAIN = "certain"
    PROBABLE = "probable"
    RISK_OF = "riskOf"
    EXTENDED = "_extended"


class SeverityEnum1(Enum):
    HIGHEST = "highest"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    LOWEST = "lowest"
    NONE = "none"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


class TrafficConstrictionTypeEnum1(Enum):
    CARRIAGEWAY_BLOCKED = "carriagewayBlocked"
    CARRIAGEWAY_PARTIALLY_OBSTRUCTED = "carriagewayPartiallyObstructed"
    LANES_BLOCKED = "lanesBlocked"
    LANES_PARTIALLY_OBSTRUCTED = "lanesPartiallyObstructed"
    ROAD_BLOCKED = "roadBlocked"
    ROAD_PARTIALLY_OBSTRUCTED = "roadPartiallyObstructed"
    EXTENDED = "_extended"


@dataclass
class InternationalIdentifier:
    class Meta:
        target_namespace = "http://levelC/schema/3/common"

    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
            "required": True,
            "max_length": 2,
        }
    )
    nationalIdentifier: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
            "required": True,
            "max_length": 1024,
        }
    )
    internationalIdentifierExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_internationalIdentifierExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
        }
    )


@dataclass
class MultilingualString:
    class Meta:
        target_namespace = "http://levelC/schema/3/common"

    values: Optional["MultilingualString.Values"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
            "required": True,
        }
    )

    @dataclass
    class Values:
        value: List[MultilingualStringValue] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://levelC/schema/3/common",
                "min_occurs": 1,
            }
        )


@dataclass
class OverallPeriod:
    class Meta:
        target_namespace = "http://levelC/schema/3/common"

    overallStartTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
            "required": True,
        }
    )
    overallEndTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
        }
    )
    overallPeriodExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_overallPeriodExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
        }
    )


@dataclass
class ConfidentialityValueEnum2:
    class Meta:
        name = "_ConfidentialityValueEnum"
        target_namespace = "http://levelC/schema/3/common"

    value: Optional[ConfidentialityValueEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class InformationDeliveryServicesEnum2:
    class Meta:
        name = "_InformationDeliveryServicesEnum"
        target_namespace = "http://levelC/schema/3/common"

    value: Optional[InformationDeliveryServicesEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class InformationStatusEnum2:
    class Meta:
        name = "_InformationStatusEnum"
        target_namespace = "http://levelC/schema/3/common"

    value: Optional[InformationStatusEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class ValidityStatusEnum2:
    class Meta:
        name = "_ValidityStatusEnum"
        target_namespace = "http://levelC/schema/3/common"

    value: Optional[ValidityStatusEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class LocationReference:
    class Meta:
        target_namespace = "http://levelC/schema/3/locationReferencing"

    locationReferenceExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationReferenceExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
        }
    )


@dataclass
class PointCoordinates:
    class Meta:
        target_namespace = "http://levelC/schema/3/locationReferencing"

    latitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
            "required": True,
        }
    )
    longitude: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
            "required": True,
        }
    )
    pointCoordinatesExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointCoordinatesExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
        }
    )


@dataclass
class AccidentCauseEnum2:
    class Meta:
        name = "_AccidentCauseEnum"
        target_namespace = "http://levelC/schema/3/situation"

    value: Optional[AccidentCauseEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class AccidentTypeEnum2:
    class Meta:
        name = "_AccidentTypeEnum"
        target_namespace = "http://levelC/schema/3/situation"

    value: Optional[AccidentTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class CollisionTypeEnum2:
    class Meta:
        name = "_CollisionTypeEnum"
        target_namespace = "http://levelC/schema/3/situation"

    value: Optional[CollisionTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class ProbabilityOfOccurrenceEnum2:
    class Meta:
        name = "_ProbabilityOfOccurrenceEnum"
        target_namespace = "http://levelC/schema/3/situation"

    value: Optional[ProbabilityOfOccurrenceEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class SeverityEnum2:
    class Meta:
        name = "_SeverityEnum"
        target_namespace = "http://levelC/schema/3/situation"

    value: Optional[SeverityEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TrafficConstrictionTypeEnum2:
    class Meta:
        name = "_TrafficConstrictionTypeEnum"
        target_namespace = "http://levelC/schema/3/situation"

    value: Optional[TrafficConstrictionTypeEnum1] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    extendedValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class HeaderInformation:
    class Meta:
        target_namespace = "http://levelC/schema/3/common"

    informationStatus: Optional[InformationStatusEnum2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
            "required": True,
        }
    )
    headerInformationExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_headerInformationExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
        }
    )


@dataclass
class PayloadPublication:
    class Meta:
        target_namespace = "http://levelC/schema/3/common"

    publicationTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
            "required": True,
        }
    )
    publicationCreator: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
            "required": True,
        }
    )
    payloadPublicationExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_payloadPublicationExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    modelBaseVersion: str = field(
        init=False,
        default="3",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    extensionName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    extensionVersion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    profileName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    profileVersion: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Validity:
    class Meta:
        target_namespace = "http://levelC/schema/3/common"

    validityStatus: Optional[ValidityStatusEnum2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
            "required": True,
        }
    )
    validityTimeSpecification: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
            "required": True,
        }
    )
    validityExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_validityExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/common",
        }
    )


@dataclass
class Location(LocationReference):
    class Meta:
        target_namespace = "http://levelC/schema/3/locationReferencing"

    coordinatesForDisplay: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
        }
    )
    locationExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_locationExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
        }
    )


@dataclass
class PointByCoordinates:
    class Meta:
        target_namespace = "http://levelC/schema/3/locationReferencing"

    bearing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
            "min_inclusive": 0,
            "max_inclusive": 359,
        }
    )
    pointCoordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
            "required": True,
        }
    )
    pointByCoordinatesExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointByCoordinatesExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
        }
    )


@dataclass
class Payload(PayloadPublication):
    class Meta:
        name = "payload"
        namespace = "http://levelC/schema/3/d2Payload"


@dataclass
class NetworkLocation(Location):
    class Meta:
        target_namespace = "http://levelC/schema/3/locationReferencing"

    networkLocationExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_networkLocationExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
        }
    )


@dataclass
class SituationRecord:
    class Meta:
        target_namespace = "http://levelC/schema/3/situation"

    situationRecordCreationTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
            "required": True,
        }
    )
    situationRecordVersionTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
            "required": True,
        }
    )
    probabilityOfOccurrence: Optional[ProbabilityOfOccurrenceEnum2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
            "required": True,
        }
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
            "required": True,
        }
    )
    locationReference: Optional[LocationReference] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
            "required": True,
        }
    )
    situationRecordExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationRecordExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PointLocation(NetworkLocation):
    class Meta:
        target_namespace = "http://levelC/schema/3/locationReferencing"

    pointByCoordinates: Optional[PointByCoordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
        }
    )
    pointLocationExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pointLocationExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/locationReferencing",
        }
    )


@dataclass
class Situation:
    class Meta:
        target_namespace = "http://levelC/schema/3/situation"

    headerInformation: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
            "required": True,
        }
    )
    situationRecord: List[SituationRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
            "min_occurs": 1,
        }
    )
    situationExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TrafficElement(SituationRecord):
    class Meta:
        target_namespace = "http://levelC/schema/3/situation"

    trafficElementExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficElementExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
        }
    )


@dataclass
class Accident(TrafficElement):
    class Meta:
        target_namespace = "http://levelC/schema/3/situation"

    accidentCause: Optional[AccidentCauseEnum2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
        }
    )
    accidentType: List[AccidentTypeEnum2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
            "min_occurs": 1,
        }
    )
    collisionType: Optional[CollisionTypeEnum2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
        }
    )
    accidentExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_accidentExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
        }
    )


@dataclass
class SituationPublication(PayloadPublication):
    class Meta:
        target_namespace = "http://levelC/schema/3/situation"

    situation: List[Situation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
        }
    )
    situationPublicationExtension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_situationPublicationExtension",
            "type": "Element",
            "namespace": "http://levelC/schema/3/situation",
        }
    )
