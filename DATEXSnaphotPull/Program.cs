using DATEXSnaphotPull.Controllers;
using DATEXSnapshotPull;
using Microsoft.OpenApi.Models;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Serialization;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddScoped<IDatexController,MyController>();

builder.Services.AddControllers()
    .AddNewtonsoftJson(options =>
    {
        options.SerializerSettings.NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore;
        options.SerializerSettings.ContractResolver = new CamelCasePropertyNamesContractResolver();
        options.SerializerSettings.Converters.Add(new StringEnumConverter
        {
            NamingStrategy = new CamelCaseNamingStrategy()
        });
    });


// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    options.UseAllOfToExtendReferenceSchemas();
    options.SupportNonNullableReferenceTypes();
    options.SwaggerDoc("v1.0.0", new OpenApiInfo { Title = "DATEX Snapshot PULL", Version = "v1.0.0" });
});

builder.Services.AddSwaggerGenNewtonsoftSupport();

var app = builder.Build();

// Configure the HTTP request pipeline.
//if (app.Environment.IsDevelopment())
//{
    app.UseSwagger(c =>
    {
        c.RouteTemplate = "datexsnapshotpull/{documentname}/openapi.json";
    });

    app.UseStaticFiles();
    app.UseSwaggerUI(c =>
    {
        //c.SwaggerEndpoint("/datexsnapshotpull/v1.0.0/openapi.json", "DATEX PULL v1.0.0");
        c.SwaggerEndpoint("/datexsnapshotpull/v1.0.0/snapshotpull-1.0.0.json", "DATEX SNapshot PULL v1.0.0");
        c.RoutePrefix = "datexsnapshotpull";
    });

//}



app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
