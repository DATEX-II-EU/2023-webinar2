using DATEXSnapshotPull;

namespace DATEXSnaphotPull.Controllers
{
    public class MyController : IDatexController
    {
        public Task<MessageContainer> PullsnapshotdataAsync(string if_Modified_Since)
        {
            MessageContainer messageContainer = new MessageContainer();
            messageContainer.Payload = new List<PayloadPublicationG>();
            PayloadPublicationG _payloadPublication = new PayloadPublicationG();
            _payloadPublication.SituationSituationPublication = new SituationPublication();
            _payloadPublication.SituationSituationPublication.Lang = "sv";
            _payloadPublication.SituationSituationPublication.PublicationTime = DateTime.Now;
            _payloadPublication.SituationSituationPublication.PublicationCreator = new InternationalIdentifier();
            _payloadPublication.SituationSituationPublication.PublicationCreator.Country = "SE";
            _payloadPublication.SituationSituationPublication.PublicationCreator.NationalIdentifier = "123";
            _payloadPublication.VersionG = "3.4";


            List<Situation> situations = new List<Situation>();
            Situation situation = new Situation();
            situation.IdG = Guid.NewGuid().ToString();
            situation.SituationRecord = new List<SituationRecordG>();
            SituationRecordG situationRecordG = new SituationRecordG();
            situationRecordG.SituationAccident = new Accident();
            situationRecordG.SituationAccident.IdG = Guid.NewGuid().ToString();
            situationRecordG.SituationAccident.VersionG = "1";
            situationRecordG.SituationAccident.SituationRecordCreationTime = DateTime.Now;
            situationRecordG.SituationAccident.SituationRecordVersionTime = DateTime.Now;
            situationRecordG.SituationAccident.ProbabilityOfOccurrence.Value = ProbabilityOfOccurrenceEnum.Certain;

            situationRecordG.SituationAccident.AccidentType = new List<AccidentTypeEnumG> { new AccidentTypeEnumG() { Value = AccidentTypeEnum.Accident } };
            situationRecordG.SituationAccident.Validity = new Validity();
            situationRecordG.SituationAccident.Validity.ValidityStatus = new ValidityStatusEnumG() { Value = ValidityStatusEnum.Active };
            situationRecordG.SituationAccident.Validity.ValidityTimeSpecification = new OverallPeriod();
            situationRecordG.SituationAccident.Validity.ValidityTimeSpecification.OverallStartTime = DateTime.Now;
            situationRecordG.SituationAccident.Validity.ValidityTimeSpecification.OverallEndTime = DateTime.Now.AddHours(2);

            situationRecordG.SituationAccident.CollisionType = new CollisionTypeEnumG() { Value = CollisionTypeEnum.CollisionWithAnimal };

            situationRecordG.SituationAccident.LocationReference = new LocationReferenceG();
            situationRecordG.SituationAccident.LocationReference.LocationReferencingPointLocation = new PointLocation();
            situationRecordG.SituationAccident.LocationReference.LocationReferencingPointLocation.CoordinatesForDisplay = new PointCoordinates();
            situationRecordG.SituationAccident.LocationReference.LocationReferencingPointLocation.CoordinatesForDisplay.Latitude = 53.01894771995707;
            situationRecordG.SituationAccident.LocationReference.LocationReferencingPointLocation.CoordinatesForDisplay.Longitude = 5.204404542910014;
            situationRecordG.SituationAccident.LocationReference.LocationReferencingPointLocation.PointByCoordinates = new PointByCoordinates();
            situationRecordG.SituationAccident.LocationReference.LocationReferencingPointLocation.PointByCoordinates.PointCoordinates = new PointCoordinates();
            situationRecordG.SituationAccident.LocationReference.LocationReferencingPointLocation.PointByCoordinates.PointCoordinates.Latitude = 53.01894771995707;
            situationRecordG.SituationAccident.LocationReference.LocationReferencingPointLocation.PointByCoordinates.PointCoordinates.Longitude = 5.204404542910014;

            situation.SituationRecord.Add(situationRecordG);
            _payloadPublication.SituationSituationPublication.Situation = situations;

            situations.Add(situation);
            _payloadPublication.SituationSituationPublication.Situation = situations;

            messageContainer.ExchangeInformation = new ExchangeInformation();
            messageContainer.ExchangeInformation.MessageType = new MessageTypeEnumG();
            messageContainer.ExchangeInformation.MessageType.Value = MessageTypeEnum.PayloadDelivery;
            messageContainer.ExchangeInformation.ExchangeContext = new ExchangeContext();
            messageContainer.ExchangeInformation.ExchangeContext.ExchangeSpecificationVersion = "1";
            messageContainer.ExchangeInformation.ExchangeContext.CodedExchangeProtocol = new ProtocolTypeEnumG() { Value = ProtocolTypeEnum.SnapshotPull };
            messageContainer.ExchangeInformation.DynamicInformation.ExchangeStatus = new ExchangeStatusEnumG();
            messageContainer.ExchangeInformation.DynamicInformation.ExchangeStatus.Value = ExchangeStatusEnum.Online;
            messageContainer.ExchangeInformation.DynamicInformation.MessageGenerationTimestamp = DateTime.Now;
            messageContainer.Payload.Add(_payloadPublication);

            return Task.FromResult(messageContainer);

        }
    }
}
