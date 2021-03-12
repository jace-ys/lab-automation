using System.Collections.Generic;
using System.Xml.Serialization;

namespace TecanSparkRelay.System
{
    [XmlRoot(ElementName = "MeasurementResultData")]
    public class MeasurementResultData
    {
        [XmlElement(ElementName = "Absorbance")]
        public Absorbance Absorbance { get; set; }
        [XmlAttribute(AttributeName = "Date")]
        public string Date { get; set; }
    }

    [XmlRoot(ElementName = "Absorbance")]
    public class Absorbance
    {
        [XmlElement(ElementName = "Summary")]
        public Summary Summary { get; set; }
        [XmlElement(ElementName = "DataLabel")]
        public DataLabel DataLabel { get; set; }
        [XmlAttribute(AttributeName = "StripIndex")]
        public string StripIndex { get; set; }
    }

    [XmlRoot(ElementName = "Summary")]
    public class Summary
    {
        [XmlElement(ElementName = "SummaryRow")]
        public List<SummaryRow> SummaryRow { get; set; }
    }

    [XmlRoot(ElementName = "SummaryRow")]
    public class SummaryRow
    {
        [XmlAttribute(AttributeName = "SettingName")]
        public string SettingName { get; set; }
        [XmlAttribute(AttributeName = "Value")]
        public string Value { get; set; }
        [XmlAttribute(AttributeName = "Unit")]
        public string Unit { get; set; }
    }

    [XmlRoot(ElementName = "DataLabel")]
    public class DataLabel
    {
        [XmlElement(ElementName = "ResultContext")]
        public List<ResultContext> ResultContext { get; set; }
        [XmlAttribute(AttributeName = "Name")]
        public string Name { get; set; }
    }

    [XmlRoot(ElementName = "ResultContext")]
    public class ResultContext
    {
        [XmlElement(ElementName = "MeasurementResult")]
        public MeasurementResult MeasurementResult { get; set; }
        [XmlAttribute(AttributeName = "PlateIndex")]
        public string PlateIndex { get; set; }
        [XmlAttribute(AttributeName = "CycleIndex")]
        public string CycleIndex { get; set; }
        [XmlAttribute(AttributeName = "WellIndex")]
        public string WellIndex { get; set; }
    }

    [XmlRoot(ElementName = "MeasurementResult")]
    public class MeasurementResult
    {
        [XmlAttribute(AttributeName = "Validation")]
        public string Validation { get; set; }
        [XmlAttribute(AttributeName = "TimeStamp")]
        public string TimeStamp { get; set; }
        [XmlAttribute(AttributeName = "Value")]
        public string Value { get; set; }
    }
}
