"""Functions for updating from Legacy to LBT."""


# the comments in the dictionaries below note whether there are plans for
# a possible better component to map the legacy one to in the future
# if the component maps to a native Grasshopper component, this is also noted
LADYBUG_MAP = {
    "Ladybug_Render View": "LB Capture View",
    "Ladybug_Import CEC Photovoltaics Module": "HB Photovoltaic Properties",  # possible better version
    "Ladybug_Outdoor Comfort Calculator": "LB UTCI Comfort",
    "Ladybug_Real Time Radiation Analysis": "LB Real Time Incident Radiation",
    "Ladybug_Draft Discomfort": None,  # SOON!
    "Ladybug_Simplified Photovoltaics Module": "HB Photovoltaic Properties",
    "Ladybug_PMV Comfort Parameters": "LB PMV Comfort Parameters",
    "Ladybug_Photovoltaics Performance Metrics": "HB Generation Loads",
    "Ladybug_Solar Water Heating Surface": None,  # possible better version
    "Ladybug_Legend Parameters": "LB Legend Parameters",
    "Ladybug_MRT Calculator": "Multiplication",  # native gh
    "Ladybug_Bioclimatic Chart": "LB Psychrometric Chart",
    "Ladybug_PV SWH System Size": None,  # possible better version
    "Ladybug_Design Day Sky Model": "LB Cumulative Sky Matrix",
    "Ladybug_Mesh Threshold Selector": "LB Mesh Threshold Selector",
    "Ladybug_Shading Mask_II": "LB Sky Mask",
    "Ladybug_Psychrometric Chart": "LB Psychrometric Chart",
    "Ladybug_Import Ground Temp": None,  # SOON!
    "Ladybug_Import Sandia Photovoltaics Module": "HB Photovoltaic Properties",  # possible better version
    "Ladybug_Wind Boundary Profile": "LB Wind Profile",
    "Ladybug_Wind Speed Calculator": "LB Wind Speed",
    "Ladybug_Passive Strategy List": "LB Passive Strategies",
    "Ladybug_SunriseSunset": "LB Day Solar Information",
    "Ladybug_CDD_HDD": "LB Degree Days",
    "Ladybug_Pedestrian Wind Comfort": None,
    "Ladybug_PMV Comfort Calculator": "LB PMV Comfort",
    "Ladybug_Ladybug": None,
    "Ladybug_SolarFan": None,  # SOON!
    "Ladybug_Import epw": "LB Import EPW",
    "Ladybug_View From Sun": "LB View From Sun",
    "Ladybug_Separate By Normal": "Evaluate Surface",  # native gh
    "Ladybug_GenCumulativeSkyMtx": "LB Cumulative Sky Matrix",
    "Ladybug_Shading Parameters List": None,
    "Ladybug_Radiation Calla Dome": "LB Radiation Dome",
    "Ladybug_F2C": "LB To SI",
    "Ladybug_Analysis Period": "LB Analysis Period",
    "Ladybug_Average Data": "LB Time Interval Operation",
    "Ladybug_Branch Data": "Partition List",  # native gh
    "Ladybug_Surface Hourly Solar": "LB Directional Solar Irradiance",
    "Ladybug_Capture View": "LB Capture View",
    "Ladybug_Set Rhino Sun": "LB Set Rhino Sun",
    "Ladybug_Open EPW And STAT Weather Files": "LB Download Weather",
    "Ladybug_Surface View Analysis": "LB View Factors",
    "Ladybug_fly": None,
    "Ladybug_SolarEnvelopeBasic": "LB Solar Envelope",
    "Ladybug_Cone Of Vision": None,
    "Ladybug_Location Finder": "LB Construct Location",
    "Ladybug_Import Location": "LB Import Location",
    "Ladybug_Cold Water Temperature": None,
    "Ladybug_Shading Mask": "LB Sky Mask",
    "Ladybug_Line Chart": "LB Monthly Chart",
    "Ladybug_Create Legend": "LB Create Legend",
    "Ladybug_Update File": "LB Sync Grasshopper File",
    "Ladybug_Beaufort Ranges": None,
    "Ladybug_DOY_HOY": "LB Calculate HOY",
    "Ladybug_Texture Maker": None,
    "Ladybug_Generate Mesh": "LB Generate Point Grid",
    "Ladybug_Import stat": "LB Import STAT",
    "Ladybug_selectSkyMtx": None,
    "Ladybug_Humidity Ratio Calculator": "LB Humidity Metrics",
    "Ladybug_Sunlight Hours Analysis": "LB Direct Sun Hours",
    "Ladybug_Clothing Function": "LB Clothing by Temperature",
    "Ladybug_3D Chart": "LB Hourly Plot",
    "Ladybug_L2G": "LB To IP",
    "Ladybug_Mesh-To-Hatch": "LB Mesh to Hatch",
    "Ladybug_Outdoor Solar Temperature Adjustor": "LB Outdoor Solar MRT",
    "Ladybug_Wind Rose": "LB Wind Rose",
    "Ladybug_Solar Water Heating System": None,  # possible better version
    "Ladybug_Cfm2M3s": "LB To SI",
    "Ladybug_Activities Met List": "LB Activities Met List",
    "Ladybug_CombineSolarEnvelopes": None,
    "Ladybug_Window Downdraft": None,
    "Ladybug_Sun_Shades_Calculator": "LB Shade Benefit",
    "Ladybug_Orient to Camera": "LB Orient to Camera",
    "Ladybug_Export Ladybug": "LB Export UserObject",
    "Ladybug_Monthly Bar Chart": "LB Monthly Chart",
    "Ladybug_Comfort Shade Benefit Evaluator": "LB Thermal Shade Benefit",
    "Ladybug_Create LB Header": "LB Construct Header",
    "Ladybug_Construct Time": "LB Calculate HOY",
    "Ladybug_uSI2uIP": "LB Unit Converter",
    "Ladybug_ShadingDesigner": "LB Shade Benefit",
    "Ladybug_Photovoltaics Surface": "HB Shade",
    "Ladybug_Separate data": "LB Deconstruct Data",
    "Ladybug_SolarFanBasic": None,  # SOON!
    "Ladybug_Tilt And Orientation Factor": None,
    "Ladybug_Wh2BTU": "LB To IP",
    "Ladybug_Radiation Rose": "LB Radiation Rose",
    "Ladybug_Bounce from Surface": "LB Surface Ray Tracing",
    "Ladybug_Shadow Study": "LB Set Rhino Sun",
    "Ladybug_Open STAT File": "File Path",  # native gh
    "Ladybug_SunPath": "LB SunPath",
    "Ladybug_uIP2uSI": "LB Unit Converter",
    "Ladybug_Passive Strategy Parameters": "LB Passive Strategy Parameters",
    "Ladybug_Body Characteristics": "LB PET Body Parameters",
    "Ladybug_BTUft2Whm": "LB To SI",
    "Ladybug_Radiation Analysis": "LB Incident Radiation",
    "Ladybug_Sunpath Shading": "HB Generation Loads",
    "Ladybug_SolarEnvelope": "LB Solar Envelope",
    "Ladybug_Clothing List": "Clothing List",
    "Ladybug_True North": None,  # SOON!
    "Ladybug_Search": None,
    "Ladybug_Update Ladybug": "LB Versioner",
    "Ladybug_Solar Water Heating Performance Metrics": None,  # possible better version
    "Ladybug_WetBulbTemp": "LB Humidity Metrics",
    "Ladybug_Adaptive Comfort Chart": "LB Adaptive Chart",
    "Ladybug_Kmz Generator": None,
    "Ladybug_View Analysis": "LB View Percent",
    "Ladybug_Residential Hot Water": "HB Service Hot Water",
    "Ladybug_North": "LB Compass",
    "Ladybug_Forward Raytracing": "LB Surface Ray Tracing",
    "Ladybug_Commercial Public Apartment Hot Water": "HB Service Hot Water",
    "Ladybug_Set the View": None,  # SOON!
    "Ladybug_DC to AC derate factor": "HB Electric Load Center",
    "Ladybug_Thermal Comfort Indices": "LB PET Comfort",
    "Ladybug_Countour Mesh": None,  # SOON!
    "Ladybug_Solar Water Heating System Detailed": "HB Service Hot Water",
    "Ladybug_Gradient Library": "LB Color Range",
    "Ladybug_Steady State Surface Temperature": None,  # SOON!
    "Ladybug_Construct Location": "LB Construct Location",
    "Ladybug_Adaptive Comfort Parameters": "LB Adaptive Comfort Parameters",
    "Ladybug_Decompose Location": "LB Deconstruct Location",
    "Ladybug_view Rose": None,  # SOON!
    "Ladybug_Orientation Study Parameters": None,
    "Ladybug_rIP2rSI": "LB Unit Converter",
    "Ladybug_Open EPW Weather File": "File Path",  # native gh
    "Ladybug_Terrain Generator": None,
    "Ladybug_C2F": "LB To IP",
    "Ladybug_ms2mph": "LB To IP",
    "Ladybug_Radiant Asymmetry Discomfort": "LB Radiant Asymmetry",
    "Ladybug_Adaptive Comfort Calculator": "LB Adaptive Comfort",
    "Ladybug_lux2ft-cd": "LB Unit Converter",
    "Ladybug_download EPW Weather File": "LB EPWmap",
    "Ladybug_Day_Month_Hour": "LB HOY to DateTime",
    "Ladybug_CDH_HDH": "LB Degree Days",
    "Ladybug_Colored Sky Visualizer": None,
    "Ladybug_BTU2Wh": "LB To SI",
    "Ladybug_Sky Dome": "LB Sky Dome",
    "Ladybug_Ankle Draft Discomfort": None,  # SOON!
    "Ladybug_Recolor Mesh": "LB Spatial Heatmap",
    "Ladybug_M3s2Cfm": "LB To IP",
    "Ladybug_Comfort Mannequin": None,
    "Ladybug_Whm2BTUft": "LB To IP"
}

HONEYBEE_MAP = {
    "Honeybee_Lookup Daylighting Folder": None,
    "Honeybee_Set Zone Properties": "HB Set Multiplier",
    "Honeybee EP context Surfaces": "HB Shade",
    "Honeybee_IES Custom Lamp": None,  # possible better version
    "Honeybee_PerimeterCoreZoning": "HB Rooms by Orientation",
    "Honeybee_Generate Cumulative Sky": "HB Cumulative Radiation",
    "Honeybee_Seasonal Schedule": "HB Seasonal Schedule",
    "Honeybee_Radiance Trans Material By Color": "HB Translucent Modifier 3",
    "Honeybee_Surface Data Based On Type": "HB Face Result by Type",
    "Honeybee_Read EP HVAC Result": "HB Read Custom Result",  # possible better version
    "Honeybee_Masses2Zones": "HB Room from Solid",
    "Honeybee_IES Project": None,  # possible better version
    "Honeybee_SplitBuildingMass2Floors": "DF Building from Solid",
    "Honeybee_Create EP Plenum": "HB Plenum",
    "Honeybee_infORventPerArea Calculator": "HB Apply Load Values",
    "Honeybee_Ambient Resolution": "HB Ambient Resolution",
    "Honeybee_Generate Test Points": "LB Generate Point Grid",
    "Honeybee_Generate Standard CIE Sky": "HB CIE Standard Sky",
    "Honeybee_Microclimate Map Analysis": None,
    "Honeybee_Decompose Based On Boundary Condition": "HB Faces by BC",
    "Honeybee_EnergyPlus Glass Material": "HB Glass Modifier",
    "Honeybee_Set Radiance Materials": "HB Apply ModifierSet",
    "Honeybee_Radiance Metal Material By Color": "HB Metal Modifier 3",
    "Honeybee_Vertical Sky Component": "HB Sky View",
    "Honeybee_AskMe": None,
    "Honeybee_Set EP Zone Construction": "HB Apply ConstructionSet",
    "Honeybee_EnergyPlus Construction": "HB Opaque Construction",
    "Honeybee_Set EnergyPlus Zone Thresholds": "HB Apply Setpoint Values",
    "Honeybee_IntersectMasses": "HB Intersect Solids",
    "Honeybee_Generate Average Sky": "HB Custom Sky",
    "Honeybee_Call from EP Construction Library": "HB Search Constructions",
    "Honeybee_simple_Inverter": "HB Electric Load Center",
    "Honeybee_Zone Attribute List": "HB Room Attributes",
    "Honeybee_Constant Schedule": "HB Constant Schedule",
    "Honeybee_R-Value With Air Films": "HB Deconstruct Construction",
    "Honeybee_orientHBGlz": "HB Facade Parameters",
    "Honeybee_Read DS Result for a point": "HB Annual Results to Data",
    "Honeybee_Therm Material": None,
    "Honeybee_Generate EP Output": "HB Simulation Output",
    "Honeybee_Get Zone EnergyPlus Loads": "HB Color Room Attributes",
    "Honeybee_Visualize Microclimate Map": "HB Visualize Thermal Map",
    "Honeybee_Make Adiabatic By Type": "HB Adiabatic by Type",
    "Honeybee_Annual Daylight Simulation": "HB Annual Daylight",
    "Honeybee_Import WINDOW Glz System": "HB Window Construction",
    "Honeybee_Surface Attribute List": "HB Face Attributes",
    "Honeybee_PET Analysis Recipe": None,  # possible better version
    "Honeybee_Therm Material to EnergyPlus Material": None,
    "Honeybee_Read HVAC Sizing": "HB Read HVAC Sizing",
    "Honeybee_OpenFileDirectory": "LB Open Directory",
    "Honeybee_Radiance BSDF Material": "HB BSDF Modifier",
    "Honeybee Lighting Density Calculator": None,
    "Honeybee_AddEarthtube": "HB HeatCool HVAC",
    "Honeybee_Set Loads And Schedules": "HB Apply ProgramType",
    "Honeybee_IES Luminaire": None,  # possible better version
    "Honeybee_Daily Schedule": "HB Gene Pool to Day Schedule",
    "Honeybee_Custom Radiant Environment": None,
    "Honeybee_Generator_PV": "HB Photovoltaic Properties",
    "Honeybee_Separate conditioned and unconditioned zones": "HB Rooms by Attribute",
    "Honeybee_addHBGlz": "HB Add Subface",
    "Honeybee_PMV Comfort Analysis Recipe": "HB PMV Comfort Map",
    "Honeybee_Read RAD Result": None,
    "Honeybee_Radiance Metal Material": "HB Metal Modifier",
    "Honeybee_Convert IMG": "HB HDR to GIF",
    "Honeybee_Get or Set HB Object Name": "HB Set Identifier",
    "Honeybee_Find Non-Convex": None,
    "Honeybee_Radiance Opaque Material": "HB Opaque Modifier",
    "Honeybee_generationsystem": "HB Electric Load Center",
    "Honeybee_Generate Sky With Certain Illuminance level": "HB Certain Illuminance",
    "Honeybee_Set EP Surface Construction": "HB Apply Opaque Construction",
    "Honeybee_DSParameters": "HB Radiance Parameter",
    "Honeybee_Decompose EnergyPlus Schedule": "HB Deconstruct Schedule",
    "Honeybee_ Run Energy Simulation": "HB Annual Loads",
    "Honeybee_MSH2RAD": "HB Shade",
    "Honeybee_Read_generation_system_results": "HB Read Generation Result",
    "Honeybee_Search EP Construction": "HB Search Constructions",
    "Honeybee_Mirror Honeybee": "HB Mirror Modifier",
    "Honeybee_Outdoor Comfort Analysis Recipe": "HB UTCI Comfort Map",
    "Honeybee_Dump Honeybee Objects": "HB Dump Objects",
    "Honeybee_Re-run OSM": "HB Run OSM",
    "Honeybee_HVAC Cooling Details": None,
    "Honeybee_OpenStudio to gbXML": "HB Dump gbXML",
    "Honeybee_Set EP Air Flow": "HB Window Opening",
    "Honeybee_Decompose EP Material": "HB Deconstruct Material",
    "Honeybee_Import THERM XML": None,
    "Honeybee_Separate Zones By Program": "HB Rooms by Attribute",
    "Honeybee_Solve Adjacencies": "HB Solve Adjacency",
    "Honeybee_Skylight Based on Ratio": "HB Skylights by Ratio",
    "Honeybee_Get EnergyPlus Schedules": "HB Deconstruct ProgramType",
    "Honeybee_Load OpenStudio Measure": "HB Load Measure",
    "Honeybee_Select by Type": "HB Faces by Type",
    "Honeybee_EnergyPlus Opaque Material": "HB Opaque Material",
    "Honeybee_Set EP Zone Interior Construction": "HB Interior Construction Subset",
    "Honeybee_Re-run IDF": "HB Run IDF",
    "Honeybee_Run Daylight Simulation": None,
    "Honeybee_Call from Radiance Library": "HB Search Modifiers",
    "Honeybee_Radiance Trans Material": "HB Translucent Modifier",
    "Honeybee_Add to EnergyPlus Library": "HB Dump Objects",
    "Honeybee_createHBZones": "HB Room",
    "Honeybee_Assembly Uvalue": "HB Deconstruct Construction",
    "Honeybee_ChangeHBObjName": "HB Set Identifier",
    "Honeybee_Glare Analysis": "HB Glare Postprocess",
    "Honeybee_Radiance Opaque Material By Color": "HB Opaque Modifier 3",
    "Honeybee_Daysim Occupancy Generator Based On List": "HB Fixed Interval Schedule",
    "Honeybee_Read All the Hourly Results from Annual Daylight Study": "HB Annual Results to Data",
    "Honeybee_Decompose Based On Type": "HB Faces by Type",
    "Honeybee_Separate Zones By Orientation": "HB Rooms by Orientation",
    "Honeybee_Radiance Materials Info": None,
    "Honeybee_Read Annual Result I": "HB Annual Daylight Metrics",
    "Honeybee_ListZonePrograms": "HB Search Programs",
    "Honeybee_createHBSrfs": "HB Face",
    "Honeybee_Energy Shade Benefit Evaluator": "HB Load Shade Benefit",
    "Honeybee_Make Adiabatic": None,
    "Honeybee_Set Exposure for HDR": "HB Adjust HDR",
    "Honeybee_bldgPrograms": "HB Building Programs",
    "Honeybee_Read Microclimate Matrix": "HB Read Thermal Matrix",
    "Honeybee_Visualise_Honeybeegeneration_cashflow": None,
    "Honeybee_HVAC Air Details": "HB All-Air HVAC",
    "Honeybee_Read THERM Result": None,
    "Honeybee_Extrude Windows": "HB Extruded Border Shades",
    "Honeybee_Daysim Electrical Lighting Use": "HB Daylight Control Schedule",
    "Honeybee_ExportEPC": None,
    "Honeybee_Generate Dark Sky": "HB Certain Illuminance",
    "Honeybee_Label Zones": "HB Label Rooms",
    "Honeybee_Convert TIF to HDR": None,
    "Honeybee_Balance Temperature Calculator": "HB Balance Temperature",
    "Honeybee_Create Therm Polygons": None,
    "Honeybee_Apply OpenStudio Measure": "HB Create OSM Measure",
    "Honeybee_Label Zone Surfaces": "HB Label Faces",
    "Honeybee_Radiance Mirror Material": "HB Mirror Modifier",
    "Honeybee_Read Annual Result II": "HB Annual Daylight Metrics",
    "Honeybee_Adaptive Comfort Analysis Recipe": "HB Adaptive Comfort Map",
    "Honeybee_Honeybee": None,
    "Honeybee_Separate Zones By Floor": "HB Rooms by Floor Height",
    "Honeybee_Glazing based on ratio": "HB Apertures by Ratio",
    "Honeybee_Refine Daylight Simulation": None,
    "Honeybee_ShadowPar": "HB Shadow Calculation",
    "Honeybee_Search EP Schedule Library": "HB Search Schedules",
    "Honeybee_Daysim Shading State": "HB Dynamic State",
    "Honeybee_Advanced Dynamic Shading Recipe": "HB Dynamic Aperture Group",
    "Honeybee_Image Based Simulation": "HB Point-In-Time View-Based",
    "Honeybee_DecomposeHBZone": "HB Deconstruct Object",
    "Honeybee_FalseColor": "HB False Color",
    "Honeybee_gbXML to Honeybee": "HB Load gbXML OSM IDF",
    "Honeybee_Create Therm Boundaries": None,
    "Honeybee_Matrix to Data Tree": "LB Deconstruct Matrix",
    "Honeybee_HVACSystemsList": "HB All-Air HVAC Templates",
    "Honeybee_Energy Simulation Par": "HB Simulation Parameter",
    "Honeybee_Indoor View Factor Calculator": None,
    "Honeybee_Daysim Occupancy Generator": "HB Weekly Schedule",
    "Honeybee_Set EnergyPlus Zone Schedules": "HB Apply Room Schedules",
    "Honeybee_Read EP Result": "HB Read Room Energy Result",
    "Honeybee_Lookup EnergyPlus Folder": None,
    "Honeybee_EnergyPlus Window Air Gap": "HB Window Gap Material",
    "Honeybee_Import WINDOW IDF Report": None,  # SOON!
    "Honeybee_Radiance Glass Material": "HB Glass Modifier",
    "Honeybee_Annual Schedule": "HB Weekly Schedule",
    "Honeybee_Watch The Sky": "HB Visualize Sky",
    "Honeybee_Thermal Autonomy Analysis": None,
    "Honeybee_Import rad": "HB Check Scene",  # possible better version
    "Honeybee_Radiance Glass Material By Color": "HB Glass Modifier 3",
    "Honeybee_EnergyPlus Window Material": "HB Window Material",
    "Honeybee_Normalize Data by Floor Area": "HB Normalize by Floor Area",
    "Honeybee_Color Surfaces by EP Result": "HB Color Faces",
    "Honeybee_Load Honeybee Objects": "HB Load Objects",
    "Honeybee_EnergyPlus Window Shade Generator": "HB Louver Shades",
    "Honeybee_RADParameters": "HB Radiance Parameter",
    "Honeybee_Generate Climate Based Sky": "HB Climatebased Sky",
    "Honeybee_Create CSV Schedule": "HB Fixed Interval Schedule",
    "Honeybee_Decompose EP Construction": "HB Deconstruct Construction",
    "Honeybee_Surface Data Based On Type Detailed": "HB Face Result by Type",
    "Honeybee_Rotate Honeybee": "HB Rotate",
    "Honeybee_Set EnergyPlus Zone Loads": "HB Apply Load Values",
    "Honeybee_Generate Zone Test Points": "HB Sensor Grid from Rooms",
    "Honeybee_Import dgp File": "HB Glare Postprocess",
    "Honeybee_Convert HDR to TIF": "HB HDR to GIF",
    "Honeybee_Radiance Mirror Material By Color": "HB Mirror Modifier 3",
    "Honeybee_Customize EnergyPlus Objects": None,
    "Honeybee_Scale Honeybee": "HB Scale",
    "Honeybee_Daysim Glare Control Recipe": "HB Aperture Group Schedule",
    "Honeybee_Read Hourly Results from Annual Daylight Study": "HB Annual Average Values",
    "Honeybee_Export To OpenStudio": "HB Model to OSM",
    "Honeybee_Color Zones by EP Result": "HB Color Rooms",
    "Honeybee_Daysim shading group sensors": "HB Aperture Group Schedule",
    "Honeybee_Daylight Factor Simulation": "HB Daylight Factor",
    "Honeybee_IES Luminaire Zone": None,  # possible better version
    "Honeybee_Conceptual Dynamic Shading Recipe": "HB Automatic Aperture Group",
    "Honeybee_Get EnergyPlus Loads": "HB Deconstruct ProgramType",
    "Honeybee_Write THERM File": None,
    "Honeybee_Remove Glazing": "HB Apertures by Ratio",
    "Honeybee_Move Honeybee": "HB Move",
    "Honeybee_EnergyPlus Shade Material": "HB Shade Material",
    "Honeybee_Condensation calculator": None,
    "Honeybee_Generate Custom Sky": "HB Custom Sky",
    "Honeybee_Call from EP Schedule Library": "HB Search Schedules",
    "Honeybee_Get Zone EnergyPlus Schedules": "HB Color Room Attributes",
    "Honeybee_Update Honeybee": "LB Versioner",
    "Honeybee_Make Adiabatic by Name": "HB Patch Missing Adjacency",
    "Honeybee_HVAC Heating Details": None,
    "Honeybee_Construct Energy Balance": "HB Thermal Load Balance",
    "Honeybee_SplitFloor2ThermalZones": "HB Straight Skeleton",
    "Honeybee_Read EP Surface Result": "HB Read Face Result",
    "Honeybee_Import idf": "HB Load gbXML OSM IDF",
    "Honeybee_Thermally Bridged EP Construction": None,
    "Honeybee_Assign HVAC System": "HB DOAS HVAC",
    "Honeybee_Convert HDR to GIF": "HB HDR to GIF",
    "Honeybee_Glazing Parameters List": "HB Facade Parameters",
    "Honeybee_Import Pts File": None,  # SOON!
    "Honeybee_Create EP Ground": "HB Ground",
    "Honeybee_Read EP Custom Result": "HB Read Custom Result",
    "Honeybee_Convert EnergyPlus Schedule to Values": "HB Schedule to Data",
    "Honeybee_Daysim Annual Profiles": "HB Annual Glare Metrics",
    "Honeybee_Add Internal Mass to Zone": "HB Internal Mass",
    "Honeybee_EnergyPlus NoMass Opaque Material": "HB Opaque Material No Mass",
    "Honeybee_Set EP Zone Underground Construction": "HB Ground Construction Subset",
    "Honeybee_Grid Based Simulation": "HB Point-In-Time Grid-Based",
    "Honeybee_Simulation Control": "HB Simulation Control",
    "Honeybee_Lighting control Recipe": "HB Daylight Control Schedule",
    "Honeybee_Add to Radiance Library": "HB Dump Objects",
    "Honeybee_Read Result Dictionary": "HB Read Result Dictionary"
}
