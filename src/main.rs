use reqwest::blocking::Client;
use serde::{Deserialize, Serialize};
use std::error::Error;
use std::io::{BufRead, BufReader};

#[derive(Debug, Deserialize, Serialize)]
struct Broadcast {
    tour: String,
    rounds: String,
}

#[derive(Debug, Deserialize, Serialize)]
struct Round {
    id: String,
    name: String,
}

fn main() -> Result<(), Box<dyn Error>> {
    let api_key: &str = "lip_DRS4U0s4YIsll0dMv5h2";
    let client: Client = Client::new();

    let base_url: String = "https://lichess.org/".to_owned();
    let func: &str = "api/broadcast";

    let request = base_url + func;

    let resp = client.get(request).bearer_auth(api_key).send()?;
    println!("Made Request!");

    let reader: BufReader<reqwest::blocking::Response> = BufReader::new(resp);

    for line_res in reader.lines() {
        let line: String = line_res?;
        // let broadcast: Broadcast = serde_json::from_str(&line)?;
        println!("{:?}", line);
    }

    Ok(())
}
