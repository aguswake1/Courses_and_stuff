var public_spreadsheet_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRPSyR6BRYCMEysw_GkHuQSbxCTFYU_iswxcDYBzgGlJPV2xTNApuEf3SJi2nsHyW4ngDRjf3LbEQ-8/pub?output=csv';

function init() {
    Papa.parse(public_spreadsheet_url, {
    download: true,
    header: true,
    complete: showInfo
    })
}

window.addEventListener('DOMContentLoaded', init)

function showInfo(results) {
    console.log(results.data);
}