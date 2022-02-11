use anyhow::{anyhow, Result};

static NANO_ERG_CONVERSION: f64 = 1000000000.0;

fn get_url() -> &'static str {
    return "https://api.coingecko.com/api/v3/simple/price?ids=ergo&vs_currencies=USD";
}

fn parse_url(coin: u8) -> String {
    let url: &str = get_url();
    if coin == 1 {
        let split = url.split("ids=").collect::<Vec<_>>();
        let substring: &str = split[1];
        let split_again = substring.split("&vs_currencies=").collect::<Vec<_>>();
        let ticker = split_again[0].to_lowercase();
        return ticker;
    } else {
        let split = url.split("ids=").collect::<Vec<_>>();
        let substring: &str = split[1];
        let split_again = substring.split("&vs_currencies=").collect::<Vec<_>>();
        let ticker = split_again[1].to_lowercase();
        return ticker;
    }
}

fn get_price_data() -> Result<u64> {
    let coin1: String = parse_url(1);
    let coin2: String = parse_url(2);
    let url: &str = get_url();
    
    let resp = reqwest::blocking::Client::new().get(url).send()?;
    let resp_json = json::parse(&resp.text()?)?;
    
    if let Some(p) = resp_json[coin1][coin2].as_f64() {
        println!("{}", p);
        return Ok(p as u64);
    } else {
        Err(anyhow!("Failed to parse price from json."))
    }
}

fn generate_current_price(data: u64) -> f64 {
    return (1.0 / data as f64) * NANO_ERG_CONVERSION;
}

fn main() {

    // let connectorName: &str = "Erg-USD";

    // let connector = FrontendConnector::new_basic_connector(
    //     connectorName,
    //     get_price_data,
        
    // )

    let _ = get_price_data();
    let _ = generate_current_price(3);

}