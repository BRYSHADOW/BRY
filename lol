local player = game.Players.LocalPlayer
local char = player.Character or player.CharacterAdded:Wait()
local humanoid = char:WaitForChild("Humanoid")

-- Lấy mô tả nhân vật
local desc = humanoid:GetAppliedDescription()

-- Scale siêu to (chỉnh số ở đây)
desc.HeadScale = 10
desc.BodyHeightScale = 10
desc.BodyWidthScale = 10
desc.BodyDepthScale = 10
desc.ProportionScale = 10
desc.BodyTypeScale = 10

-- Áp dụng
humanoid:ApplyDescription(desc)
