def getRustFileHeader():
    raw = """use anyhow::{anyhow, Result};

static NANO_ERG_CONVERSION: f64 = 1000000000.0;

"""
    return raw

def getRustFileUrl(url):
    raw = "static BASE_URL: &'static str = " + str(url) + ";"
    return raw

def getRestRustFile():
    raw = """

fn parse_url(coin: u8) -> String {
    let url: &str = BASE_URL;
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
    let url: &str = BASE_URL;
    
    let resp = reqwest::blocking::Client::new().get(url).send()?;
    let resp_json = json::parse(&resp.text()?)?;
    
    if let Some(p) = resp_json[coin1][coin2].as_f64() {
        let nanoerg_price = (1.0 / p) * NANO_ERG_CONVERSION;
        println!("Price (Erg): {}", p);
        println!("Price (NanoErg): {}", nanoerg_price);
        return Ok(nanoerg_price as u64);
    } else {
        Err(anyhow!("Failed to parse price from json."))
    }
}

fn generate_current_price(data: u64) -> f64 {
    let price: f64 = (1.0 / data as f64) * NANO_ERG_CONVERSION;
    println!("{}", price);
    return price;
}

fn main() {

    // let connectorName: &str = "Erg-USD";

    // let connector = FrontendConnector::new_basic_connector(
    //     connectorName,
    //     get_price_data,
        
    // )

    // connector.run();

    let _ = get_price_data();
    let _ = generate_current_price(3);

}
"""
    return raw

def getRawCargoTomlFile():
    raw = """[package]
name = "connector-builder"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
json            = "0.12.4"
reqwest         = { version = "0.10.7", features = ["blocking"] }
anyhow          = "1.0.32"
openssl = { version = "0.10", features = ["vendored"] }
"""
    return raw