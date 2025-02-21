loadstring(game:HttpGet(("https://raw.githubusercontent.com/daucobonhi/Ui-Redz-V2/refs/heads/main/UiREDzV2.lua")))()

       local Window = MakeWindow({
         Hub = {
         Title = "BRY LR",
         Animation = "FB: Chau Mcbr"
         },
        Key = {
        KeySystem = false,
        Title = "Key System",
        Description = "",
        KeyLink = "",
        Keys = {"1234"},
        Notifi = {
        Notifications = true,
        CorrectKey = "Running the Script...",
       Incorrectkey = "The key is incorrect",
       CopyKeyLink = "Copied to Clipboard"
      }
    }
  })

       MinimizeButton({
       Image = "http://www.roblox.com/asset/?id=96114075322069",
       Size = {35, 35},
       Color = Color3.fromRGB(10, 10, 10),
       Corner = true,
       Stroke = false,
       StrokeColor = Color3.fromRGB(255, 0, 0)
      })
      
------ Tab
     local Tab1o = MakeTab({Name = "Script Farm"})
     local Tab2o = MakeTab({Name = "Script Lumtrai"})
------- BUTTON
    
    AddButton(Tab1o, {
     Name = "Redz Hub",
    Callback = function()
	  local Settings = {
  JoinTeam = "Pirates"; -- Pirates/Marines
  Translator = true; -- true/false
}

loadstring(game:HttpGet("https://raw.githubusercontent.com/realredz/BloxFruits/refs/heads/main/Source.lua"))(Settings)
  end
  })
  AddButton(Tab2o, {
     Name = "lumtraitudoisv",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/marisdeptrai/Script-Free/main/FruitFinder.lua"))()
  end
  })
  AddButton(Tab1o, {
     Name = "Volcano Hub",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/wpisstestfprg/Volcano/refs/heads/main/VolcanoLocal.lua", true))()
  end
  })
  AddButton(Tab2o, {
     Name = "hack dieu chinh",
    Callback = function()
	  loadstring(Game:HttpGet("https://raw.githubusercontent.com/VanThanhIOS/OniiChanVanThanhIOS/refs/heads/main/oniichanpakavanthanhios"))()
  end
  })
  AddButton(Tab1o, {
     Name = "Script Trẩu",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/LuaCrack/TrauHub/refs/heads/main/TrauXt"))()
  end
  })
  AddButton(Tab1o, {
     Name = "Rubu RedZ Hub",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/LuaCrack/RubuRoblox/refs/heads/main/RubuBF"))()
  end
  })
  AddButton(Tab1o, {
     Name = "ASTRAL Hub",
    Callback = function()
	  loadstring(game:HttpGet("https://raw.githubusercontent.com/Overgustx2/Main/refs/heads/main/BloxFruits_25.html"))()
  end
  })