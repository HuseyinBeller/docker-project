def cut_corpses():
    
    # Find the weapon by type ID in the player's backpack or equipped items
    weapon = Items.FindByID(0x26BD, -1, Player.Backpack.Serial, True)
    
    if not weapon:
        # If not found in backpack, check if it's equipped
        weapon = Player.GetItemOnLayer('LeftHand') or Player.GetItemOnLayer('RightHand')
        if weapon and weapon.ItemID != 0x0F52:
            weapon = None
    
    if not weapon:
        Player.HeadMessage(33, "Weapon of type 0x26BD not found!")
        return
    
    # Get all corpses in the area
    corpse_filter = Items.Filter()
    corpse_filter.IsCorpse = True
    corpse_filter.OnGround = True
    corpse_filter.RangeMax = 2
    
    corpses = Items.ApplyFilter(corpse_filter)
    
    for corpse in corpses:
        # Use the weapon on the corpse
        Items.UseItem(weapon)
        Target.WaitForTarget(1000)
        Target.TargetExecute(corpse)
        Misc.Pause(1000)  # Wait a second before moving to the next corpse
        
        # Look for and pick up any "The Head Of" items
        collect_heads()

def collect_heads():
    # Create a filter for head items on the ground
    head_filter = Items.Filter()
    head_filter.OnGround = True
    head_filter.RangeMax = 2
    head_filter.Name = "The Head Of"  # Filter by name
    
    # Get all heads in the area
    heads = Items.ApplyFilter(head_filter)
    
    for head in heads:
        Player.HeadMessage(66, f"Found head: {head.Name}")
        Items.Move(head, Player.Backpack, 0)
        Misc.Pause(600)  # Wait for server response


if __name__ == "__main__":
    cut_corpses() 