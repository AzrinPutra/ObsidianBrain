# XML, XSL, XSD Summary - CSIT 128

## Files
- A2.xml — weather forecast XML for Singapore, 6 <weather> entries under <forecast>
- S2.xsl — XSL stylesheet linked via <?xml-stylesheet?>

## XSL Bugs Fixed
1. `:` instead of `=` in attribute declarations
2. Duplicate `select` on one `<xsl:value-of>`
3. `queryLocation`/`queryTime` are attributes — need `@` and `forecast/` prefix
4. Chrome blocks local XSLT — use Firefox or `python3 -m http.server 8000`

## XSD Structure Built
```xml
<xsd:element name="forecast">
  <xsd:element name="weather" minOccurs="0" maxOccurs="unbounded">
    year (integer)
    month (1-12)
    date (1-31)
    dayOfWeek (enumeration: Mon/Tue/Wed/Thur/Fri/Sat/Sun)
    overall (string)
    overallCode (string)
    highest (integer)
    lowest (integer)
    @yyyymmdd (string)
    @queryLocation (string)
    @queryTime (string)
  </xsd:element>
</xsd:element>
```

## XSL Concepts Covered
- `match="/"` — runs once at root, builds page shell
- `match="weather"` — runs once per weather entry (6 times)
- `xsl:apply-templates select="forecast/weather"` — triggers Template 2 from Template 1
- `xsl:sort` — self-closing, goes inside apply-templates
- `xsl:if test="dayOfWeek = 'Mon'"` — conditional per day column
- `xsl:text` — for literal text/spaces between value-of calls
- `xsl:choose/xsl:when` — convert month number to name (e.g., 11 → Nov)

## Calendar Grid XSL Structure
- Template 1: page shell + table headers + apply-templates
- Template 2: one `<tr>` per weather entry
  - Date column with month/date
  - 7 day columns using `xsl:if test="dayOfWeek = 'Mon'"` etc.