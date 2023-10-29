using CSClient;
using CSClient.DatexSnapshotPull;
using Newtonsoft;
using Newtonsoft.Json;

using var httpClient = new HttpClient();
Client client = new Client(httpClient);
client.BaseUrl = "https://datexopenapi.azurewebsites.net/datexsnapshotpull/1.0.0";
Task<MessageContainer> messageContainer = client.PullsnapshotdataAsync("");
messageContainer.Wait();
string output = JsonConvert.SerializeObject(messageContainer.Result, Formatting.Indented);
Console.WriteLine(output);

Accident accident = messageContainer.Result.Payload.First().SituationSituationPublication.Situation.First().SituationRecord.First().SituationAccident;

Console.WriteLine("ID: {0}", accident.IdG);
Console.WriteLine("AccidentType: {0}", accident.AccidentType.First().Value);
Console.WriteLine("CollisionType: {0}", accident.CollisionType.Value);
Console.ReadLine();

